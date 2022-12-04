from django.shortcuts import render
from django.contrib.auth.decorators import *
from django.http import HttpResponseRedirect
from django.urls import reverse
import inspect
from . import forms
from . import models

# Create your views here.
def active_check(user):
	return user.is_active

@login_required
@user_passes_test(active_check)
def index(request):
	return render(request, 'Table.html',
	{
		'items': models.Base.objects.all(),
		'user': models.User.objects.get(username=request.user.username)
	})

@login_required
@user_passes_test(active_check)
def detail(request):
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

@login_required
@user_passes_test(active_check)
def new(request):
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

@login_required
@user_passes_test(active_check)
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

@login_required
@user_passes_test(active_check)
def delete(request):
	try:
		user = models.User.objects.get(username=request.user.username)
		item = models.Base.objects.get(id=request.GET['id'])
		if user.username == item.publisher:
			item.delete()
		return HttpResponseRedirect(reverse('item:index'))
	except:
		return HttpResponseRedirect(reverse('item:index'))

@login_required
@user_passes_test(active_check)
def categlories(request):
	return render(request, 'Categlory.html', {'categlories': [cate for cate, _ in inspect.getmembers(models, inspect.isclass) if not cate in ['Base', 'User']]})

@login_required
@user_passes_test(active_check)
def categlory(request, cate):
	items = getattr(models, cate).objects.all()
	attrs = [attr for attr in [field.name for field in getattr(models, cate)._meta.get_fields()] if attr not in [field.name for field in models.Item._meta.get_fields()]]
	return render(request, 'Table.html',
	{
		'items': items,
		'extra': {attr: [getattr(item, attr) for item in items] for attr in attrs},
		'user': models.User.objects.get(username=request.user.username)
	})