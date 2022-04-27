from django.shortcuts import render
from Shop.models import Product
from django.contrib.auth.decorators import login_required
from Commerce.forms import BillingDetailsForm, ShippingDetailsForm
from Commerce.models import Customer, Cart, Order, OrderItem, Coupon_Code, Delivery_Charge
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from datetime import datetime

def custom_pc(request):
    # Get processsor
    processor = Product.objects.filter(subcategory__iexact = 'processor')

    motherboard = Product.objects.filter(subcategory__iexact = 'motherboard')

    graphics_card = Product.objects.filter(subcategory__iexact = 'graphics card')
    
    ram= Product.objects.filter(subcategory__iexact = 'ram')

    primary_storage = Product.objects.filter(subcategory__iexact = 'primary storage')

    secondary_storage = Product.objects.filter(subcategory__iexact = 'secondary storage')

    psu = Product.objects.filter(subcategory__iexact = 'psu')

    case = Product.objects.filter(subcategory__iexact = 'case')

    cpu_cooler = Product.objects.filter(subcategory__iexact = 'cpu cooler')

    context = {'processor' : processor, 'motherboard' : motherboard, 'graphics_card' : graphics_card,
    'ram' : ram, 'primary_storage' : primary_storage, 'secondary_storage' : secondary_storage,
    'psu' : psu, 'case' : case, 'cpu_cooler' : cpu_cooler}

    return render(request, 'custom_pc.html', context)


@login_required
def custom_pc_checkout(request):
    # Render two forms 
    if request.method == 'GET':   
        form = BillingDetailsForm()
        shipform = ShippingDetailsForm()

        customer = Customer.objects.filter(user = request.user)
        if customer:
            for c in customer:
                form.fields['first_name'].initial = c.first_name
                form.fields['last_name'].initial = c.last_name
                form.fields['locality'].initial = c.locality
                form.fields['city'].initial = c.city
                form.fields['zipcode'].initial = c.zipcode
                form.fields['province'].initial = c.province
                form.fields['phone'].initial = c.phone
                form.fields['customer_pan_number'].initial = c.customer_pan_number
                form.fields['alternative_phone_number'].initial = c.alternative_phone_number        

        return render(request, 'custom_pc_checkout.html', {'form' : form, 'shipform':shipform})

    elif request.method == 'POST':
        user = request.user
        #now = datetime.now()

        place_order = json.loads(request.body)

        # Check coupon validity
        if place_order['action'] == 'check-coupon':
            coupon = Coupon_Code.objects.filter(code__iexact = place_order['coupon'], active = True)
            if coupon:
                data = {'valid': 'yes'}
                return JsonResponse(data, content_type = 'application/json')

            else:
                data = {'valid': 'no'}
                return JsonResponse(data, content_type = 'application/json')    


        elif place_order['action'] == 'checkout':
            subtotal_price = 0
            # Get the subtotal price of the cart
            processor_id = int(place_order['processor_id'])
            motherboard_id = int(place_order['motherboard_id'])
            graphics_id = int(place_order['graphics_id'])
            ram_id = int(place_order['ram_id'])
            ram_quantity = int(place_order['ram_quantity'])
            primary_id = int(place_order['primary_id'])
            secondary_id = int(place_order['secondary_id'])
            secondary_quantity = int(place_order['secondary_quantity'])
            case_id = int(place_order['case_id'])
            cooler_id = int(place_order['cooler_id'])
            psu_id = int(place_order['psu_id'])

            processor = Product.objects.get(id = processor_id)
            subtotal_price = subtotal_price + processor.current_price

            motherboard = Product.objects.get(id = motherboard_id)
            subtotal_price = subtotal_price + motherboard.current_price

            graphics = Product.objects.get(id = graphics_id)
            subtotal_price = subtotal_price + graphics.current_price

            ram = Product.objects.get(id = ram_id)
            subtotal_price = subtotal_price + (ram.current_price * ram_quantity)

            primary = Product.objects.get(id = primary_id)
            subtotal_price = subtotal_price + primary.current_price

            secondary = Product.objects.get(id = secondary_id)
            subtotal_price = subtotal_price + (secondary.current_price * secondary_quantity)

            case = Product.objects.get(id = case_id)
            subtotal_price = subtotal_price + case.current_price

            cooler = Product.objects.get(id = cooler_id)
            subtotal_price = subtotal_price + cooler.current_price
            
            psu = Product.objects.get(id = psu_id)
            subtotal_price = subtotal_price + psu.current_price

            _subtotal = subtotal_price    

            # Add coupon code discount (if any)
            if place_order['coupon_code']!='':
                ccode = Coupon_Code.objects.filter(code__iexact = place_order['coupon_code'], active = True)
                if ccode:
                    for c in ccode:
                        minimum_expense = c.minimum_expense
                        discount = c.discount
        
                    discount_amount = (discount/100) * subtotal_price    

                    subtotal_price = subtotal_price - discount_amount
                    coupon_code = place_order['coupon_code']

            else:
                discount_amount = 0
                coupon_code = ''
                       
                    

            # Get the appropriate delivery charge
            delivery_charge = Delivery_Charge.objects.all()
            if delivery_charge:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
                for d in delivery_charge:
                    min_exp = d.minimum_expense
                    if subtotal_price < min_exp:
                        delivery_charge = d.price
                    else:
                        delivery_charge = 0 

            else:
                print('is js')
                delivery_charge = 0               

            # Get the total price
            total_price = subtotal_price + delivery_charge 

            new_order = Order.objects.create(user = user,
            payment_method = place_order['payment_method'],
            subtotal_price = _subtotal,
            Coupon_used = coupon_code,
            discount_amount = discount_amount,
            total_paid_price = total_price,
            delivery_charge = delivery_charge,
            order_type = 'Custom PC Build'
            )

            # Add Billing Address Data
            new_order.billingaddress_set.create(
                first_name = place_order['first_name'],
                last_name = place_order['last_name'],
                locality = place_order['locality'],
                city = place_order['city'],
                zipcode = place_order['zipcode'],
                province = place_order['province'],
                phone = place_order['phone'],
                alternative_phone_number = place_order['alternative_phone_number'],
                customer_pan_number = place_order['customer_pan_number'],
            )  

            # Add Shipping Address Data
            new_order.shippingaddress_set.create(
                first_name = place_order['ship_first_name'],
                last_name = place_order['ship_last_name'],
                locality = place_order['ship_locality'],
                city = place_order['ship_city'],
                zipcode = place_order['ship_zipcode'],
                province = place_order['ship_province'],
                phone = place_order['ship_phone'],
                alternative_phone_number = place_order['ship_alternative_phone_number'],
                pickup_address = place_order['ship_pickup_address'],
                special_notes = place_order['ship_special_notes']
            ) 


            new_order.orderitem_set.create(product = processor, quantity = 1, unit_price = processor.current_price, total_price = processor.current_price) 
            new_order.orderitem_set.create(product = motherboard, quantity = 1, unit_price = motherboard.current_price, total_price = motherboard.current_price)
            new_order.orderitem_set.create(product = graphics, quantity = 1, unit_price = graphics.current_price, total_price = graphics.current_price)
            new_order.orderitem_set.create(product = ram, quantity = ram_quantity, unit_price = ram.current_price, total_price = ram.current_price * ram_quantity)
            new_order.orderitem_set.create(product = primary, quantity = 1, unit_price = primary.current_price, total_price = primary.current_price)
            new_order.orderitem_set.create(product = secondary, quantity = secondary_quantity, unit_price = secondary.current_price, total_price = secondary.current_price * secondary_quantity)
            new_order.orderitem_set.create(product = case, quantity = 1, unit_price = case.current_price, total_price = case.current_price)
            new_order.orderitem_set.create(product = cooler, quantity = 1, unit_price = cooler.current_price, total_price = cooler.current_price)
            new_order.orderitem_set.create(product = psu, quantity = 1, unit_price = psu.current_price, total_price = psu.current_price)



            data = {'orderid': new_order.id}

            return JsonResponse(data, content_type = 'application/json')        
        
    return render(request, 'custom_pc_checkout.html',{'form' : form, 'shipform':shipform})    
