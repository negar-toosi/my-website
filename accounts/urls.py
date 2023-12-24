from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_view

app_name = 'accounts'
urlpatterns = [
    path('login/',views.login_views,name='login'),
    path('logout/',views.logout_views,name='logout'),
    path('signup/',views.signup_views,name='signup'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]  