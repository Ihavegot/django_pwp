from django import forms


class AddOrderForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, label='Telefon kontaktowy')
    adres = forms.CharField(max_length=100, required=True, label='Adres dostarczenia')
    info = forms.CharField(widget=forms.Textarea)