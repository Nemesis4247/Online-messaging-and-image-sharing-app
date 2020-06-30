from .models import *
from django import forms

class PhoneForm(forms.ModelForm):
    phone = forms.CharField(max_length = 13)

# try to make this form in input html
class MessageForm(forms.ModelForm):
    Text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model = Messages
        exclude = ["From", "date_time"]

class MessageForm2(forms.ModelForm):
    class Meta():
        model = Messages
        exclude = ["date_time"]
