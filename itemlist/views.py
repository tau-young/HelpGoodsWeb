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
	if request.method == 'POST':
		form = forms.NewItemForm(request.POST)
		if form.is_valid():
			categlory = form.cleaned_data['categlory']
			itemname = form.cleaned_data['itemname']
			description = form.cleaned_data['description']
			publisher = form.cleaned_data['publisher']
			address = form.cleaned_data['address']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			models.Item.create(categlory, itemname, description, publisher, address, phone, email).save()
			return HttpResponseRedirect(reverse('itemlist:index'))
		return render(request, 'NewItem.html', {'form': form})
	user = models.User.objects.get(username=request.user.username)
	form = forms.NewItemForm(initial=
	{
		'categlory': 'Item',
		'publisher': user.username,
		'address': user.address,
		'phone': user.phone,
		'email': user.email
	})
	return render(request, 'NewItem.html', {'form': form})