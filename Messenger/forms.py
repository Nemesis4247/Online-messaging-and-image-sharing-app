from .models import *
from django import forms


class MessageForm(forms.ModelForm):
    Text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model = Messages
        exclude = ["From", "date_time"]

class MessageForm2(forms.ModelForm):
    class Meta():
        model = Messages
        exclude = ["date_time"]
