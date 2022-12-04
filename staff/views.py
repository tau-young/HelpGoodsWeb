from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
	# if request.user.is_staff
	return HttpResponse('Staff')