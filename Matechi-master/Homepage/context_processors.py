from Commerce.models import Cart, Delivery_Charge, Coupon_Code,Order
from Categories.models import Category
from online_users.models import OnlineUserActivity
from django.contrib.auth.models import User


def admin_index_processors(request):
    user_activity_objects = OnlineUserActivity.get_user_activities()
    number_of_active_users = user_activity_objects.count()

    total_users = (User.objects.count())

    # Generating sales report
    ind_products = 0
    transactions = 0
    product_sales = {}
    order = Order.objects.all()
    for o in order:
        transactions += 1
        items = o.orderitem_set.all()
        
        for i in items:
            print(str(i.product))
            if str(i.product) not in product_sales:
                product_sales[str(i.product)] = i.quantity
            else:
                product_sales[str(i.product)] = product_sales[str(i.product)] + i.quantity      

    print((product_sales)) 

    # Find indv product sales
    for pv in product_sales.values():
        ind_products += int(pv)  
  

    print(ind_products)
    print(transactions)    
        
    context = {'online_users' : number_of_active_users, 'total_users' : total_users, 'ind_products' : ind_products, 'transactions' : transactions}
    return context

def base_message_processors(request):
    if request.user.is_authenticated:
        user = request.user

        # Get the subtotal price of the cart
        cart_items = Cart.objects.filter(user = user)
        if cart_items:
            subtotal_price = 0
            for c in cart_items:
                subtotal_price = subtotal_price + c.quantity * c.product.current_price

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
    
            # Get the total quantity
            cart_items = Cart.objects.filter(user = user)
            total_quantity = 0
            quantity = Cart.objects.filter(user = request.user)
            if quantity:
                for q in quantity:
                    total_quantity = total_quantity + q.quantity

            return {'total_quantity' : total_quantity, 'cart_items' : cart_items, 'subtotal_price' : subtotal_price, 'total_price': total_price, 'delivery_charge' : delivery_charge}   

        else:
            return {'total_quantity' : 0, 'cart_items' : 0, 'subtotal_price' : 0, 'total_price': 0, 'delivery_charge' : 0}  

    else:
        return {}  


def navbar_message_processors(request):
    category_list =  Category.objects.all().order_by('priority')
    
    if category_list:
        return {'category' : category_list}
    else:
        return {'category' : ''}             