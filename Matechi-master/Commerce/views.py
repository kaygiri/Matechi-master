from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerRegistrationForm, CustomerProfileForm, ProfileSetupForm, ShippingDetailsForm, BillingDetailsForm
from django.views import View
from django.contrib import messages
from .models import Customer, Cart, Order, OrderItem, Coupon_Code, Delivery_Charge
from Shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from datetime import datetime

def profile_setup(request):
    if request.method == 'GET':
        form = ProfileSetupForm()
        context = {'form' : form}
        return render(request, 'profilesetup.html', context)

    if request.method == 'POST':
        # get the model from the db                                                
        customer = Customer.objects.filter(user = request.user)
        # If there exists no customer make one 
        if not customer:
            form = ProfileSetupForm(request.POST)
            if form.is_valid():
                user = request.user
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name'] 
                locality = form.cleaned_data['locality'] 
                city = form.cleaned_data['city'] 
                zipcode = form.cleaned_data['zipcode'] 
                province = form.cleaned_data['province'] 
                phone = form.cleaned_data['phone'] 
                customer_pan_number = form.cleaned_data['customer_pan_number']
                alternative_phone_number = form.cleaned_data['alternative_phone_number']  
                #Now save this
                reg = Customer(user = user, first_name=first_name, last_name = last_name, locality=locality, city=city, zipcode=zipcode, province=province, phone=phone, alternative_phone_number = alternative_phone_number, customer_pan_number =customer_pan_number)
                reg.save()

                return HttpResponseRedirect("/profile/")

        else: 
            # If profile is already set up then update
            customer_instance = Customer.objects.get(user = request.user)        
            form = CustomerProfileForm(request.POST, instance = customer_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Congratulations !! Profile Updated Successfully')
                billing_address = Customer.objects.filter(user = request.user)
                context = {'form' : form, 'bill_add' : billing_address}

            return render(request, 'profile.html', context)  


@login_required
def profile(request):
    order = Order.objects.filter(user = request.user,complete = False).order_by('-ordered_date')
    previous_orders = Order.objects.filter(user = request.user).order_by('-ordered_date')
    if request.method == 'GET':

        # This is for editing form.
        # Populate the form field with default values to be changed while submiting
        form = CustomerProfileForm()

        customer = Customer.objects.filter(user = request.user)
        for c in customer:
                    form.fields['first_name'].initial = c.first_name
                    form.fields['last_name'].initial = c.last_name
                    form.fields['locality'].initial = c.locality
                    form.fields['city'].initial = c.city
                    form.fields['zipcode'].initial = c.zipcode
                    form.fields['province'].initial = c.province
                    form.fields['phone'].initial = c.phone
                    form.fields['alternative_phone_number'].initial = c.alternative_phone_number
                    form.fields['customer_pan_number'].initial = c.customer_pan_number
 


        billing_address = Customer.objects.filter(user = request.user)

        context = {'form' : form, 'bill_add' : billing_address, 'order' : order, 'previous_orders' : previous_orders}
        return render(request, 'profile.html', context)

    # This is for updating the form
    elif request.method == 'POST':
        
        # get the model from the db                                                
        customer = Customer.objects.filter(user = request.user)
        # If there exists no customer make one 
        if not customer:
            form = CustomerProfileForm(request.POST)
            if form.is_valid():
                user = request.user
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name'] 
                locality = form.cleaned_data['locality'] 
                city = form.cleaned_data['city'] 
                zipcode = form.cleaned_data['zipcode'] 
                province = form.cleaned_data['province'] 
                phone = form.cleaned_data['phone']
                customer_pan_number = form.cleaned_data['customer_pan_number']
                alternative_phone_number = form.cleaned_data['alternative_phone_number']     
                #Now save this
                reg = Customer(user = user, first_name=first_name, last_name = last_name, locality=locality, city=city, zipcode=zipcode, province=province, phone=phone, customer_pan_number = customer_pan_number, alternative_phone_number = alternative_phone_number)
                reg.save()

                return HttpResponseRedirect("/profile/")

        else: 
            # If profile is already set up then edit and update
            customer_instance = Customer.objects.get(user = request.user)        
            form = CustomerProfileForm(request.POST, instance = customer_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Congratulations !! Profile Updated Successfully')
                billing_address = Customer.objects.filter(user = request.user)
                context = {'form' : form, 'bill_add' : billing_address, 'order':order}

            return render(request, 'profile.html', context)

def register(request):
    if request.method == 'GET':
        form = CustomerRegistrationForm()
        return render(request, 'register.html', {'form' : form})

    elif request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registration Successfully')
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return HttpResponseRedirect("/profile-setup/")    

        else:
            return render(request,'register.html',{'form':form})    



@login_required
def add_to_cart(request):
    user = request.user

    if request.method == 'GET':
        return render(request, 'cart.html')

    if request.method == 'POST':
        product_details = json.loads(request.body)
        product_id = product_details['productId']
        quantity = product_details['quantity']
        product = Product.objects.get(id = product_id)

        # Check if the cart from the user fro a particular product is created before 
        previous_cart = Cart.objects.filter(user = user, product = product)
        if previous_cart:
            previous_cart2 = Cart.objects.get(user = user, product = product)
            previous_cart2.quantity= previous_cart2.quantity + int(quantity)
            previous_cart2.save()       
        else:    
            cart, created = Cart.objects.get_or_create(user = user, product = product, quantity = quantity)

            #Cart(user = user, product = product, quantity = quantity)
            cart.save()

        return HttpResponse(json.dumps({'job':'done'}))    

@login_required
def update_cart(request):
    user = request.user

    if request.method == 'POST':
        product_details = json.loads(request.body)
        product_id = product_details['productId']
        quantity = product_details['quantity']
        action = product_details['action']
        product = Product.objects.get(id = product_id)

        if (action == 'update'):
            if int(quantity) == 0:
                previous_cart = Cart.objects.filter(user = user, product = product)
                previous_cart.delete()

            else:    
                previous_cart = Cart.objects.get(user = user, product = product)
                previous_cart.quantity = quantity
                previous_cart.save()

        elif (action == 'delete'):
            previous_cart = Cart.objects.get(user = user, product = product)
            previous_cart.delete()       

        return HttpResponse(json.dumps({'job': 'done'}))    


@login_required
def checkout(request):

    if request.method == 'GET':
        # render empty form if get
        # Check if there are no items in the cart
        # If there are no items

        cart_items = Cart.objects.filter(user = request.user)
        if not cart_items:
            print('There are no items')
        else:    
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

            return render(request, 'checkout.html', {'form' : form, 'shipform':shipform})                


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
            # Get the subtotal price of the cart
            cart_items = Cart.objects.filter(user = user)
            subtotal_price = 0
            for c in cart_items:
                subtotal_price = subtotal_price + c.quantity * c.product.current_price

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
                for d in delivery_charge:
                    min_exp = d.minimum_expense
                    if subtotal_price < min_exp:
                        delivery_charge = d.price
                    else:
                        delivery_charge = 0 

            else:
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
            order_type = 'Normal'
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

            # Get what is in the cart
            cart = Cart.objects.filter(user = user)

            # Find the unit price and total price
            for c in cart:
                unit_price = c.product.current_price
                total_price = unit_price * c.quantity
                new_order.orderitem_set.create(product = c.product, quantity = c.quantity, unit_price = unit_price, total_price = total_price) 

                # Reduce available units from the product model
                #product = Product.objects.get(product_name__icontains = c.product)
                c.product.quantity = c.product.quantity - int(c.quantity)
                if (c.product.quantity < 0):
                    c.product.quantity = 0
                c.product.save()    

            # Delete items from the cart after checkout
            cart = Cart.objects.filter(user = user).delete()




            data = {'orderid': new_order.id}

            return JsonResponse(data, content_type = 'application/json')

    return render(request, 'checkout.html')        
 

@login_required
def invoice(request, orderID):
    user = request.user
    if user.is_superuser:
        order = Order.objects.filter(id = orderID)

    else:    
        order = Order.objects.filter(id = orderID, user = request.user)

    context = {'order':order}        
    return render(request, 'invoice.html', context)  


        


