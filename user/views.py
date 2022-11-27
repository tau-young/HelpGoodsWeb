from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def index(request):
	if 'user' not in request.session:
		request.session['user'] = ''
	return render(request, 'UserInfo.html',
	{
		'user': request.session['user']
		# 'user': User.objects.all()
	})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			if username == password:
				request.session['user'] = username
				return HttpResponseRedirect(reverse('user:index'))
			else:
				return render(request, 'Login.html',
				{
					'form': form,
					'message': 'Username or Password Incorrect!'
				})
	return render(request, 'Login.html',
	{
		'form': LoginForm()
	})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			address = form.cleaned_data['address']
			contactInfo = form.cleaned_data['contactInfo']
			if password1 == password2:
				request.session['user'] = username
				return HttpResponseRedirect(reverse('user:login'))
			else:
				return render(request, 'Login.html',
				{
					'form': form,
					'message': 'Passwords do not match!'
				})
	return render(request, 'Login.html',
	{
		'form': RegisterForm()
	})

def userInfo(request, username):
	user = username
	return render(request, 'UserInfo.html',
	{
		'user': user
	})