from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms
from . import models

# Create your views here.
def active_check(user):
	return user.is_active

@login_required
def index(request):
	user = models.User.objects.get(username=request.user.username)
	return render(request, 'UserInfo.html',
	{
		'user': user,
		'is_active': request.user.is_active,
		'is_staff': request.user.is_staff
	})

def login_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:index'))
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse('user:index'))
			else:
				return render(request, 'Login.html',
				{
					'form': form,
					'message': 'Username and password do not match!'
				})
	return render(request, 'Login.html', {'form': forms.LoginForm()})

def logout_view(reqeset):
	logout(reqeset)
	return HttpResponseRedirect(reverse('user:login'))

def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:index'))
	if request.method == 'POST':
		form = forms.RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			cpassword = form.cleaned_data['cpassword']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			if password != cpassword:
				message = 'Passwords do not match!'
			if models.User.objects.filter(username=username):
				message = 'Username taken!'
			if 'message' in locals():
				return render(request, 'Register.html',
				{
					'form': form,
					'message': message
				})
			user = User.objects.create_user(username, email, password)
			user.is_active = False
			user.save()
			models.User.create(username, address, phone, email).save()
			return HttpResponseRedirect(reverse('user:login'))
		return render(request, 'Register.html', {'form': form})
	return render(request, 'Register.html', {'form': forms.RegisterForm()})

@login_required
@user_passes_test(active_check)
def info(request, username):
	try:
		user = models.User.objects.get(username=username)
		return render(request, 'UserInfo.html',
		{
			'user': user,
			'is_active': request.user.is_active,
			'is_staff': request.user.is_staff
		})
	except:
		return HttpResponseRedirect(reverse('user:index'))