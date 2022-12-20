from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import inspect
from . import models
import item.models

# Create your views here.
@staff_member_required
def index(request):
	inactive_users = []
	for user in User.objects.filter(is_active=False):
		inactive_users.append(models.User.objects.get(username=user.username))
	return render(request, 'Index.html',
	{
		'inactive': inactive_users,
		'categlories': [cate for cate, _ in inspect.getmembers(item.models, inspect.isclass) if not cate in ['Base', 'User']]
	})

@staff_member_required
def approve(request):
	user = User.objects.get(username=request.GET['username'])
	user.is_active = True
	user.save()
	return HttpResponseRedirect(reverse('staff:index'))

@staff_member_required
def reject(request):
	User.objects.get(username=request.GET['username']).delete()
	models.User.objects.get(username=request.GET['username']).delete()
	return HttpResponseRedirect(reverse('staff:index'))

@staff_member_required
def new(request):
	return HttpResponse('New Categlory')