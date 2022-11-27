from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
	return HttpResponse('User View')

def login(request):
	return render(request, "login.html",
	{
		"form": LoginForm()
	})