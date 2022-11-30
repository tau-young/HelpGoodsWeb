from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
	return render(request, 'Table.html',
	{
		'items': models.Item.objects.all()
	})

def detail(request):
	return render(request, 'Detail.html', { 'item': models.Item.objects.get(id=request.GET['id'])})