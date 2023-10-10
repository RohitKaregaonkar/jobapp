from django import forms


class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name", help_text="Enter First Name")
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, disabled=True)