import re
from django import forms
from django.core.exceptions import ValidationError

class SigninForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'Email is a required field'})
    password = forms.CharField(required=True,
                              error_messages={'required': 'Password is a required field'},
                             widget=forms.PasswordInput()
    )



    #custom fields validation

    def clean_password(self):
        #import pdb;
        #pdb.set_trace()
        password = re.compile('[\d\w]{4,}', re.I)
        if not password.match(self.cleaned_data['password']):
            raise forms.ValidationError('Allowed only digits _ and fsd')

        return self.cleaned_data['password']