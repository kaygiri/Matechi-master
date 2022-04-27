from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from Commerce import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
 
urlpatterns = [
    path('profile-setup/', views.profile_setup, name = 'profile_setup'),
    path('profile/', views.profile, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name = 'passwordchange.html', form_class = MyPasswordChangeForm), name = 'passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name = 'passwordchangedone.html'), name = 'password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html', form_class = MyPasswordResetForm), name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html', form_class = MySetPasswordForm), name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name = 'password_reset_complete'),
    path('cart/', views.add_to_cart, name = 'cart'),
    path('update-cart/', views.update_cart, name = 'update-cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('invoice/<int:orderID>/',views.invoice, name = 'invoice'),
    ] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)