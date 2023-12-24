from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth import get_user_model

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username or Email')
    

    # def clean(self):
    #     user_model = get_user_model()
    #     username_or_email = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     if username_or_email and password:
    #         username_or_email = user_model._default_manager.filter(
    #         Q(**{user_model.USERNAME_FIELD: username_or_email}) 
    #         | Q(email__iexact=username_or_email)
    #     )
    #     user = authenticate(email=username_or_email, password=password) 
    #     return self.cleaned_data


