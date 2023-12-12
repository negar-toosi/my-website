from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from accounts.backends import EmailOrUsernameModelBackend



# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm         
def login_views(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request,data=request.POST)
        
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:  
                login(request,user) 
                return redirect('/')
            else:
                username_or_email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = EmailOrUsernameModelBackend.authenticate(request, email=username_or_email, password=password)
                if user is not None:  
                    login(request,user) 
                    return redirect('/')
                else:
                    print('user not found')

    else:
        form = CustomAuthenticationForm()
    
    context = {'form':form}
    return render(request,'accounts/login.html',context)
@login_required
def logout_views(request):
    
    logout(request)
    return redirect('/')

def signup_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
            
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        redirect('/')