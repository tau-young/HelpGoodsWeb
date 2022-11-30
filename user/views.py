from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	return render(request, 'UserInfo.html')

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('user:index'))
		else:
			return render(request, 'Login.html',
			{
				'message': 'Invalid Credentials'
			})
	return render(request, 'Login.html')

def logout_view(reqeset):
	logout(reqeset)
	return HttpResponseRedirect(reverse('user:login'))

def register(request):
	if request.session.get('is_login', None):
		return HttpResponseRedirect(reverse('user:index'))
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		address = request.POST['address']
		contactInfo = request.POST['contactInfo']
		if password1 != password2:
			message = 'Passwords do not match!'
		if models.User.objects.filter(username=username):
			message = 'Username taken!'
		if 'message' in locals():
			return render(request, 'Register.html', {'message': message})
		newUser = models.User()
		newUser.username = username
		newUser.password = password1
		newUser.address = address
		newUser.contactInfo = contactInfo
		newUser.save()
		return HttpResponseRedirect(reverse('user:login'))
	return render(request, 'Register.html')