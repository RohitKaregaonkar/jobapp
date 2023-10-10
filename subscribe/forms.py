from django import forms

def validate_comma(value):
    if "," in value:
        raise forms.ValidationError("Invalid Name")
    return value

class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name", help_text="Enter First Name")
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, disabled=True)
    
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if "," in data:
            raise forms.ValidationError("Invalid First Name")
        return data