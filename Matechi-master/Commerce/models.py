from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from Shop.models import Product
from django.core.exceptions import ValidationError
from datetime import datetime

PROVINCE_CHOICES = (
    ('Province No. 1', 'Province No. 1'),
    ('Province No. 2', 'Province No. 2'),
    ('Bagmati', 'Bagmati'),
    ('Gandaki', 'Gandaki'),
    ('Lumbini', 'Lumbini'),
    ('Karnali', 'Karnali'),
    ('Sudurpashchim', 'Sudurpashchim'),
)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Processing', 'Processing'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Cancelled', 'Cancelled')
)

class Delivery_Charge(models.Model):
    price = models.IntegerField()
    minimum_expense = models.IntegerField()


class Coupon_Code(models.Model):
    code = models.CharField(max_length = 200, blank = True, null = True)
    discount = models.IntegerField(verbose_name = 'Discount in percentage')
    minimum_expense = models.IntegerField()
    created_on = models.DateTimeField(default = datetime.now(), verbose_name = 'Created On') 
    valid_until = models.DateTimeField(verbose_name = 'Valid Until')
    active = models.BooleanField(default = True)   

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField(blank = True, null = True)
    province = models.CharField(choices = PROVINCE_CHOICES, max_length = 100)
    phone = models.BigIntegerField()
    customer_pan_number = models.BigIntegerField(blank = True, null = True)
    alternative_phone_number = models.BigIntegerField(blank = True, null = True)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_cart_item(self):
        return self.quantity * self.product.current_price   


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_type = models.CharField(max_length = 50, blank = True, null = True)
    ordered_date = models.DateTimeField(auto_now_add = True)

    payment_method = models.CharField(max_length = 100, blank = False, null = False)
    subtotal_price = models.PositiveBigIntegerField()
    Coupon_used = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Coupon Code Used')
    discount_amount = models.PositiveBigIntegerField(blank = True, null = True, verbose_name = 'Discount Amount')
    delivery_charge = models.PositiveBigIntegerField(blank = True, null = True, verbose_name = 'Delivery Charge')

    total_paid_price = models.PositiveBigIntegerField()
    status = models.CharField(max_length = 50, choices = STATUS_CHOICES, default = 'Order Placed')  
    complete = models.BooleanField(default = False)
    cancel_reason = models.TextField(blank = True, null = True, verbose_name = 'Cancel Reason (Only to be filled when order is cancelled)')


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField(blank = True, null = True)
    province = models.CharField(choices = PROVINCE_CHOICES, max_length = 100)
    phone = models.BigIntegerField()
    alternative_phone_number = models.BigIntegerField(blank = True, null = True)
    pickup_address = models.TextField()
    special_notes = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.locality + ',' + self.city  

class BillingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField(blank = True, null = True)
    province = models.CharField(choices = PROVINCE_CHOICES, max_length = 100)
    phone = models.BigIntegerField()
    customer_pan_number = models.BigIntegerField(blank = True, null = True)
    alternative_phone_number = models.BigIntegerField(blank = True, null = True)

    def __str__(self):
        return self.locality + ',' + self.city    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity =  models.PositiveIntegerField(default = 1)

    unit_price = models.IntegerField()
    total_price = models.IntegerField()
    #status = models.CharField(max_length = 50, choices = STATUS_CHOICES, default = 'Pending')

    def __str__(self):
        return str(self.product)










