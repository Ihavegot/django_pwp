from django import forms
from django.contrib.auth.forms import UserCreationForm


class AddOrderForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, label='Telefon kontaktowy')
    adres = forms.CharField(max_length=100, required=True, label='Adres dostarczenia')
    info = forms.CharField(widget=forms.Textarea)


class SignUpFormLabels(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpFormLabels, self).__init__(*args, **kwargs)
