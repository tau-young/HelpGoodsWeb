from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from . import forms, models
import json

# Create your views here.
@staff_member_required
def index(request):
	inactive_users = []
	for user in User.objects.filter(is_active=False):
		inactive_users.append(User.objects.get(username=user.username))
	return render(request, 'Index.html',
	{
		'inactive': inactive_users,
		'categlories': [cate.name for cate in models.Category.objects.all()]
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
	if request.method == 'POST':
		form = forms.NewCategoryForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			attributes = form.cleaned_data['attributes'].split('\r\n') if form.cleaned_data['attributes'] else ''
			models.Category.create(name, json.dumps(attributes)).save()
			return HttpResponseRedirect(reverse('staff:index'))
		return render(request, 'NewCategory.html', {'form': form})
	return render(request, 'NewCategory.html', {'form': forms.NewCategoryForm()})