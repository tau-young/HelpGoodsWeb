from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
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
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		address = request.POST['address']
		contactInfo = request.POST['contactInfo']
		if password1 == password2:
			request.session['user'] = username
			return HttpResponseRedirect(reverse('user:login'))
		else:
			return render(request, 'Register.html',
			{
				'message': 'Passwords do not match!'
			})
	return render(request, 'Register.html')