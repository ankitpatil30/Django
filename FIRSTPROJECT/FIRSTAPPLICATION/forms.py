from django import forms
from django.core import validators

def check(value):
    if len(value)<5:
        raise forms.ValidationError("Length of password should be greater than 5")

# def check(value):
#     if value[0].lower != 'a':
#         raise forms.ValidationError("Name should start with 'a'"), validators=[check]

# def check(value):
#     if(value[0].lower != 'a'):
#         raise forms.ValidationError("NAme should start with a")


class Signupform(forms.Form):
    first_name=forms.CharField(label="First Name")
    last_name=forms.CharField(label="Last Name")
    email=forms.EmailField(max_length=40)
    verify_email=forms.EmailField(label="Verify email")
    password=forms.CharField(widget=forms.PasswordInput, validators=[check])
    # password=forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(6)])

# Task = Provide a custom validator to the password field 
# where password should have atleast 
# 1 special, 1 upper case, 1 numeric characters

def checkemail(self):
    email=self.cleaned_date['email']
    vmail=self.cleaned_data['verify_email']

    if email != vmail:
        raise forms.ValidationError("Your email doesn't match")





   
        

