from django import forms


# fields are taken from here in crm/views.py
class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
