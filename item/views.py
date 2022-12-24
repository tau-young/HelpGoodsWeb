from django.shortcuts import render
from django.contrib.auth.decorators import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms, models
from staff.models import Category
import json

# Create your views here.
def active_check(user):
	return user.is_active

@login_required
@user_passes_test(active_check)
def index(request):
	return render(request, 'Table.html',
	{
		'category': 'Item',
		'items': models.Item.objects.all(),
		'user': models.User.objects.get(username=request.user.username),
		'staff': request.user.is_staff,
	})

@login_required
@user_passes_test(active_check)
def detail(request):
	item = models.Item.objects.get(id=request.GET['id'])
	attrs = json.loads(Category.objects.get(name=item.category).attributes)
	return render(request, 'Detail.html',
	{
		'item': item,
		'attrs': attrs,
		'extra': {attr: json.loads(item.extra)[attr] for attr in attrs},
	})

@login_required
@user_passes_test(active_check)
def new(request, category=''):
	if not category:
		return render(request, 'New.html', {'categlories': [cate.name for cate in Category.objects.all()]})
	user = models.User.objects.get(username=request.user.username)
	attributes = {attr: '' for attr in json.loads(Category.objects.get(name=category).attributes)}
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			category = form.cleaned_data['category']
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			item = models.Item.create(category, name, description, user.username, address, phone, email)
			attributes = {attr: request.POST[attr.replace(' ', '_')] for attr, _ in attributes.items()}
			item.extra = json.dumps(attributes)
			item.save()
			return HttpResponseRedirect(reverse('item:index'))
		return render(request, 'NewItem.html',
		{
			'category': category,
			'form': form,
			'attributes': attributes.items(),
		})
	return render(request, 'NewItem.html',
	{
		'category': category,
		'form': forms.NewItemForm(initial={
			'category': category,
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
			'category': category,
			'form': form,
			'attributes': attributes.items(),
			'item': item,
		})
	return render(request, 'EditItem.html',
	{
		'id': request.GET['id'],
		'category': category,
		'form': forms.NewItemForm(initial={
			'category': item.category,
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
		item = models.Item.objects.get(id=request.GET['id'])
		if user.username == item.publisher or request.user.is_staff: item.delete()
		return HttpResponseRedirect(reverse('item:index'))
	except:
		return HttpResponseRedirect(reverse('item:index'))

@login_required
@user_passes_test(active_check)
def category(request, category=''):
	if not category:
		return render(request, 'Category.html', {'categlories': [cate.name for cate in Category.objects.all()]})
	items = models.Item.objects.filter(category=category)
	attrs = json.loads(Category.objects.get(name=category).attributes)
	return render(request, 'Table.html',
	{
		'category': category,
		'items': items,
		'extra': {attr: [json.loads(item.extra)[attr] for item in items] for attr in attrs},
		'user': models.User.objects.get(username=request.user.username),
		'staff': request.user.is_staff,
	})