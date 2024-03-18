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
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

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
                next_url = request.POST.get('next', '/')
                return redirect(next_url)      
            else:
                username_or_email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = EmailOrUsernameModelBackend.authenticate(request, email=username_or_email, password=password)
                if user is not None:  
                    login(request,user) 
                    next_url = request.POST.get('next', '/')
                    return redirect(next_url)
        else:
            messages.add_message(request,messages.ERROR,'your username or password was wrong')

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

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Request'
                    email_template_name = 'accounts/password_message.txt'
                    parameters = {
                        'email' : user.email,
                        'domain' : '127.0.0.1:8000/',
                        'site_name' : 'mywebsite',
                        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                        'token' : default_token_generator.make_token(user),
                        'protocol' : 'http'

                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False)
                    except:
                        return HttpResponse('Invalid header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm()
    context = {
        'password_form':password_form,
    }
    return render(request,'accounts/password_reset.html',context)