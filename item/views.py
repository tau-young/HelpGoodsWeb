from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import inspect
from . import forms
from . import models

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	return render(request, 'Table.html',
	{
		'items': models.Base.objects.all(),
		'user': models.User.objects.get(username=request.user.username)
	})

def detail(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	try:
		item = models.Base.objects.get(id=request.GET['id'])
		item = getattr(models, item.categlory).objects.get(id=request.GET['id'])
		attrs = [attr for attr in [field.name for field in getattr(models, item.categlory)._meta.get_fields()] if attr not in [field.name for field in models.Item._meta.get_fields()]]
		return render(request, 'Detail.html',
		{
			'item': item,
			'attrs': attrs,
			'extra': {attr: getattr(item, attr) for attr in attrs},
		})
	except:
		return HttpResponseRedirect(reverse('item:index'))

def new(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	user = models.User.objects.get(username=request.user.username)
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			categlory = form.cleaned_data['categlory']
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			getattr(models, categlory).create(categlory, name, description, user.username, address, phone, email).save()
			return HttpResponseRedirect(reverse('item:index'))
		return render(request, 'NewItem.html', {'form': form})
	form = forms.NewItemForm(initial=
	{
		'categlory': 'Item',
		'address': user.address,
		'phone': user.phone,
		'email': user.email,
	})
	return render(request, 'NewItem.html', {'form': form})

def edit(request):
	try:
		user = models.User.objects.get(username=request.user.username)
		item = models.Base.objects.get(id=request.GET['id'])
		if user.username != item.publisher:
			return HttpResponseRedirect(reverse('item:index'))
		if request.method == 'POST':
			form = forms.NewItemForm(request.POST)
			if form.is_valid():
				item.categlory = form.cleaned_data['categlory']
				item.name = form.cleaned_data['name']
				item.description = form.cleaned_data['description']
				item.address = form.cleaned_data['address']
				item.phone = form.cleaned_data['phone']
				item.email = form.cleaned_data['email']
				item.save()
				return HttpResponseRedirect(reverse('item:index'))
			return render(request, 'EditItem.html', {'form': form, 'item': item})
		form = forms.NewItemForm(initial=
		{
			'categlory': item.categlory,
			'name': item.name,
			'description': item.description,
			'address': item.address,
			'phone': item.phone,
			'email': item.email,
		})
		return render(request, 'EditItem.html', {'form': form, 'item': item})
	except:
		return HttpResponseRedirect(reverse('item:index'))

def delete(request):
	try:
		user = models.User.objects.get(username=request.user.username)
		item = models.Base.objects.get(id=request.GET['id'])
		if user.username == item.publisher:
			item.delete()
		return HttpResponseRedirect(reverse('item:index'))
	except:
		return HttpResponseRedirect(reverse('item:index'))

def categlories(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	return render(request, 'Categlory.html', {'categlories': [cate for cate, _ in inspect.getmembers(models, inspect.isclass) if not cate in ['Base', 'User']]})

def categlory(request, cate):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('user:login'))
	items = getattr(models, cate).objects.all()
	attrs = [attr for attr in [field.name for field in getattr(models, cate)._meta.get_fields()] if attr not in [field.name for field in models.Item._meta.get_fields()]]
	return render(request, 'Table.html',
	{
		'items': items,
		'extra': {attr: [getattr(item, attr) for item in items] for attr in attrs},
		'user': models.User.objects.get(username=request.user.username)
	})