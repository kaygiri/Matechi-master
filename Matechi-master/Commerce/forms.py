from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer,ShippingAddress,BillingAddress

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class' : 'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password(again)', widget = forms.PasswordInput(attrs = {'class' : 'form-control'}))
    email = forms.CharField(required = True, widget = forms.EmailInput(attrs = {'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'}
        widgets = {'username': forms.TextInput(attrs = {'class' : 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {'autofocus' : True, 'class' : 'form-control'}))
    password = forms.CharField(label = _('Password'), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'current-password', 'class' : 'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = _("Old Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'current-password', 'autofocus' : True, 'class' : 'form-control'}))
    new_password1 = forms.CharField(label = _("New Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'new-password','class' : 'form-control'}), help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label = _("Confirm New Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class' : 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label = _("Email"), max_length = 254, widget = forms.EmailInput(attrs = {'autocomplete' : 'email', 'class' : 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = _("New Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'new-password','class' : 'form-control'}), help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label = _("Confirm New Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class' : 'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','locality', 'city', 'zipcode', 'province', 'phone', 'customer_pan_number', 'alternative_phone_number']
        widgets = {'first_name' : forms.TextInput(attrs = {'class' : 'form-control','placeholder':'asdf'}),
        'last_name' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'locality' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'city' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'province' : forms.Select(attrs = {'class' : 'form-control'}),
        'zipcode' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'phone' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'customer_pan_number' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'alternative_phone_number' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        }

class ProfileSetupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','locality', 'city', 'zipcode', 'province', 'phone', 'customer_pan_number', 'alternative_phone_number']
        widgets = {'first_name' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'last_name' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'locality' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'city' : forms.TextInput(attrs = {'class' : 'form-control'}),
        'province' : forms.Select(attrs = {'class' : 'form-control'}),
        'zipcode' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'phone' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'customer_pan_number' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        'alternative_phone_number' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        }

class ShippingDetailsForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress      
        fields = ['first_name','last_name','locality', 'city', 'zipcode', 'province', 'phone','alternative_phone_number', 'pickup_address', 'special_notes']
        widgets = {
        'first_name' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true','id':'ship_first_name'}),
        'last_name' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true','id':'ship_last_name'}),
        'locality' : forms.TextInput(attrs = {'class' : 'form-control required-form','id':'ship_locality'}),
        'city' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true','id':'ship_city'}),
        'province' : forms.Select(attrs = {'class' : 'form-control required-form','required':'true','id':'ship_province'}),
        'zipcode' : forms.NumberInput(attrs = {'class' : 'form-control','id':'ship_zipcode'}),
        'phone' : forms.NumberInput(attrs = {'class' : 'form-control required-form','required':'true','id':'ship_phone'}),
        'alternative_phone_number' : forms.NumberInput(attrs = {'class' : 'form-control','id':'ship_alternative_phone_number'}),
        'pickup_address' : forms.Textarea(attrs = {'class' : 'form-control required-form','rows':10, 'cols':100,'required':'true','id':'ship_pickup_address'}),
        'special_notes' : forms.Textarea(attrs = {'class' : 'form-control','rows':10, 'cols':100,'id':'ship_special_notes'}),
        }

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingAddress      
        fields = ['first_name','last_name','locality', 'city', 'zipcode', 'province', 'phone','customer_pan_number','alternative_phone_number']
        widgets = {
        'first_name' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true', 'id':'bill_first_name'}),
        'last_name' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true', 'id':'bill_last_name'}),
        'locality' : forms.TextInput(attrs = {'class' : 'form-control required-form', 'id':'bill_locality'}),
        'city' : forms.TextInput(attrs = {'class' : 'form-control required-form','required':'true', 'id':'bill_city'}),
        'province' : forms.Select(attrs = {'class' : 'form-control required-form','required':'true', 'id':'bill_province'}),
        'zipcode' : forms.NumberInput(attrs = {'class' : 'form-control', 'id':'bill_zipcode'}),
        'phone' : forms.NumberInput(attrs = {'class' : 'form-control required-form','required':'true', 'id':'bill_phone'}),
        'customer_pan_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'id':'bill_customer_pan_number'}),
        'alternative_phone_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'id':'bill_alternative_phone_number'}),
        }            