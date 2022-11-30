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
		'items': models.Item.objects.all(),
		'user': models.User.objects.get(username=request.user.username)
	})

def detail(request):
	return render(request, 'Detail.html', {'item': models.Item.objects.get(id=request.GET['id'])})

def new(request):
	user = models.User.objects.get(username=request.user.username)
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			categlory = form.cleaned_data['categlory']
			itemname = form.cleaned_data['itemname']
			description = form.cleaned_data['description']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			models.Item.create(categlory, itemname, description, user.username, address, phone, email).save()
			return HttpResponseRedirect(reverse('itemlist:index'))
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
	user = models.User.objects.get(username=request.user.username)
	item = models.Item.objects.get(id=request.GET['id'])
	if user.username != item.publisher:
		return HttpResponseRedirect(reverse('itemlist:index'))
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			item.categlory = form.cleaned_data['categlory']
			item.itemname = form.cleaned_data['itemname']
			item.description = form.cleaned_data['description']
			item.address = form.cleaned_data['address']
			item.phone = form.cleaned_data['phone']
			item.email = form.cleaned_data['email']
			item.save()
			return HttpResponseRedirect(reverse('itemlist:index'))
		return render(request, 'EditItem.html', {'form': form, 'item': item})
	form = forms.NewItemForm(initial=
	{
		'categlory': item.categlory,
		'itemname': item.itemname,
		'description': item.description,
		'address': item.address,
		'phone': item.phone,
		'email': item.email,
	})
	return render(request, 'EditItem.html', {'form': form, 'item': item})

def delete(request):
	user = models.User.objects.get(username=request.user.username)
	item = models.Item.objects.get(id=request.GET['id'])
	if user.username == item.publisher:
		item.delete()
	return HttpResponseRedirect(reverse('itemlist:index'))