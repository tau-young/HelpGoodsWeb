from django import forms
from phonenumber_field.formfields import PhoneNumberField

class LoginForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput())
	cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
	address = forms.CharField(label='Address')
	# phone = PhoneNumberField(region='CN')
	phone = forms.CharField(label = 'Phone Number')
	email = forms.EmailField()