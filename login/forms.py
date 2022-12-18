from login.models import FormData
from django import forms


class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


class FormDataForm(forms.ModelForm):
    
    model = FormData
    name = forms.CharField()
    email = forms.EmailField()
    fields = ['Last_name', 'First_name', 'Account_Number', 'Amount']
