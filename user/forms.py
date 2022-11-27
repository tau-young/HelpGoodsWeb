from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password')

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username')
	password1 = forms.CharField(label='Password')
	password2 = forms.CharField(label='Confirm Password')
	address = forms.CharField(label='Address')
	contactInfo = forms.CharField(label='Contact Info')