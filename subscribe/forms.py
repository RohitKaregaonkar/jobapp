from django import forms


class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)