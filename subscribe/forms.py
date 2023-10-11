from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model =  Subscribe
        # fields = ['first_name', 'last_name', 'email']
        fields = '__all__'
        # exclude = ('first_name',)
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'option': _('Subscription Option'),
        }
        error_messages = {
            'first_name': {
                'required': _('Compulsory Field')
            }
        }
        # help_texts = {
        #     'first_name': _('Enter Characters Only')
        # }


# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid Name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="First Name", help_text="Enter First Name")
#     last_name = forms.CharField(max_length=100, required=False, validators=[validate_comma])
#     email = forms.EmailField(max_length=100, disabled=True, validators=[validate_comma])
    
#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid First Name")
#         return data