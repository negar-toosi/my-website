from django import forms
from mysite.models import content,newsletter
from captcha.fields import CaptchaField
class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class cantactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = content
        fields = '__all__'

class newsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'