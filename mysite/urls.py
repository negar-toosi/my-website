from django.urls import path
from .views import *
from . import views
from django.conf import settings
app_name = 'mysite'


urlpatterns = [
    path('',index_view,name='index'),
    path('contact',contact_view,name='contact'),
    path('about',about_view,name='about'),
    path('newsletter',newsletter_view,name='newsletter'),
    path('test',test,name='test'),
]
