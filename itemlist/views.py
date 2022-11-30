from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from . import models

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	return render(request, 'Table.html',
	{
		'items': models.Item.objects.all()
	})

def detail(request):
	return render(request, 'Detail.html', {'item': models.Item.objects.get(id=request.GET['id'])})

def new(request):
	return render(request, 'NewItem.html', {'form': forms.NewItemForm.create(models.User.objects.get(username=request.user.username))})