from django.urls import path,include
from . import views
from django.contrib import admin


app_name = 'accounts'
urlpatterns = [
    path('login/',views.login_views,name='login'),
    path('logout/',views.logout_views,name='logout'),
    path('signup/',views.signup_views,name='signup'),
    path('password_reset/',views.password_reset_views,name='password_reset'),
    
]  