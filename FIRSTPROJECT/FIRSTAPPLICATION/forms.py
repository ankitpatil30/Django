from django import forms

class Signupform(forms.Form):
    first_name=forms.CharField(label="First Name")
    last_name=forms.CharField(label="Last Name")
    email=forms.EmailField(max_length=40)
    password=forms.CharField(widget=forms.PasswordInput)

