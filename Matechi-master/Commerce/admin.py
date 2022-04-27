from django.contrib import admin
from .models import Customer, Cart, OrderItem, Order, BillingAddress, ShippingAddress,Delivery_Charge, Coupon_Code
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'locality', 'city', 'zipcode', 'province'] 

@admin.register(Cart)
class ProductmodelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'last_modified']

@admin.register(Delivery_Charge)
class DeliveryChargeAdmin(admin.ModelAdmin):
    list_display = ['price', 'minimum_expense']    

    def has_add_permission(self, request):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Coupon_Code)
class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount','minimum_expense','created_on','valid_until','active'] 
    list_per_page = 20    


class BillingAddressInline(admin.StackedInline):
    model = BillingAddress  
    max_num = 1
    classes = ['tab-billing-address']

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress     
    max_num = 1
    classes = ['tab-shipping-address']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    classes = ['tab-items']

class OrderAdmin(DjangoTabbedChangeformAdmin, admin.ModelAdmin):
    list_display = ['user', 'ordered_date', 'status', 'complete']    
    list_per_page = 20
    list_filter = ('complete','ordered_date')
    search_fields = ('id',)
    inlines = [BillingAddressInline, ShippingAddressInline, OrderItemInline]

    fieldsets = (
    ('Order Status', {
         'classes': ('tab-order-status',),
        'fields': ('status', 'complete', 'cancel_reason')
    }),
   )

    tabs = [
        ("Items", ["tab-items"]),
        ("Status", ["tab-order-status"]),
        ("Shipping Address", ["tab-shipping-address"]),
        ("Billing Address", ["tab-billing-address"]),
    ]


admin.site.register(Order, OrderAdmin)    
