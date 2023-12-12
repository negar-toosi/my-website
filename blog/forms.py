from django import forms
from blog.models import Comments
from captcha.fields import CaptchaField

class commentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','subject','email','message','post']
