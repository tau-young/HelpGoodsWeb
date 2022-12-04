from django.urls import path
from . import views

app_name = 'stuff'
urlpatterns = [
	path('', views.index, name='index'),
]