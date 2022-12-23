from django.shortcuts import render
from django.contrib.auth.decorators import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms, models
from staff.models import Categlory
import json

# Create your views here.
def active_check(user):
	return user.is_active

@login_required
@user_passes_test(active_check)
def index(request):
	return render(request, 'Table.html',
	{
		'categlory': 'Item',
		'items': models.Base.objects.all(),
		'user': models.User.objects.get(username=request.user.username)
	})

@login_required
@user_passes_test(active_check)
def detail(request):
	item = models.Item.objects.get(id=request.GET['id'])
	attrs = json.loads(Categlory.objects.get(name=item.categlory).attributes)
	return render(request, 'Detail.html',
	{
		'item': item,
		'attrs': attrs,
		'extra': {attr: json.loads(item.extra)[attr] for attr in attrs},
	})

@login_required
@user_passes_test(active_check)
def new(request, categlory=''):
	if not categlory:
		return render(request, 'New.html', {'categlories': [cate.name for cate in Categlory.objects.all()]})
	user = models.User.objects.get(username=request.user.username)
	attributes = {attr: '' for attr in json.loads(Categlory.objects.get(name=categlory).attributes)}
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			categlory = form.cleaned_data['categlory']
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			item = models.Item.create(categlory, name, description, user.username, address, phone, email)
			attributes = {attr: request.POST[attr.replace(' ', '_')] for attr, _ in attributes.items()}
			item.extra = json.dumps(attributes)
			item.save()
			return HttpResponseRedirect(reverse('item:index'))
		return render(request, 'NewItem.html',
		{
			'categlory': categlory,
			'form': form,
			'attributes': attributes.items(),
		})
	return render(request, 'NewItem.html',
	{
		'categlory': categlory,
		'form': forms.NewItemForm(initial={
			'categlory': categlory,
			'address': user.address,
			'phone': user.phone,
			'email': user.email,
		}),
		'attributes': attributes.items(),
	})

@login_required
@user_passes_test(active_check)
def edit(request):
	user = models.User.objects.get(username=request.user.username)
	item = models.Item.objects.get(id=request.GET['id'])
	attributes = json.loads(item.extra)
	if user.username != item.publisher:
		return HttpResponseRedirect(reverse('item:index'))
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.address = form.cleaned_data['address']
			item.phone = form.cleaned_data['phone']
			item.email = form.cleaned_data['email']
			attributes = {attr: request.POST[attr.replace(' ', '_')] for attr, _ in attributes.items()}
			item.extra = json.dumps(attributes)
			item.save()
			return HttpResponseRedirect(reverse('item:index'))
		return render(request, 'EditItem.html',
		{
			'id': request.GET['id'],
			'categlory': categlory,
			'form': form,
			'attributes': attributes.items(),
			'item': item,
		})
	return render(request, 'EditItem.html',
	{
		'id': request.GET['id'],
		'categlory': categlory,
		'form': forms.NewItemForm(initial={
			'categlory': item.categlory,
			'name': item.name,
			'description': item.description,
			'address': item.address,
			'phone': item.phone,
			'email': item.email,
		}),
		'attributes': attributes.items(),
		'item': item,
	})

@login_required
@user_passes_test(active_check)
def delete(request):
	try:
		user = models.User.objects.get(username=request.user.username)
		item = models.Base.objects.get(id=request.GET['id'])
		if user.username == item.publisher: item.delete()
		return HttpResponseRedirect(reverse('item:index'))
	except:
		return HttpResponseRedirect(reverse('item:index'))

@login_required
@user_passes_test(active_check)
def categlory(request, categlory=''):
	if not categlory:
		return render(request, 'Categlory.html', {'categlories': [cate.name for cate in Categlory.objects.all()]})
	items = models.Item.objects.filter(categlory=categlory)
	attrs = json.loads(Categlory.objects.get(name=categlory).attributes)
	return render(request, 'Table.html',
	{
		'categlory': categlory,
		'items': items,
		'extra': {attr: [json.loads(item.extra)[attr] for item in items] for attr in attrs},
		'user': models.User.objects.get(username=request.user.username),
	})