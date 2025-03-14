
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
class SignUpForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter email-username", "class": "form-control"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address", "class": "form-control"}))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"}))
    class Meta:    
        model = get_user_model()
        fields = ['username','email', 'password1','password2' ]  
        