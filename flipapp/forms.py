from django import forms
from django.contrib.auth.models import User
from .import models
from .models import Customer

class CustomerUserform(forms.ModelForm):
    class meta:
        model= User 
        fields =['first name','last name','user name','password']
widgets={
    'password':forms.PasswordInput()
    }

class Customerform(forms.modelform):
    class meta:
        model= Customer
        fields =['address','mobile','profile_pic']