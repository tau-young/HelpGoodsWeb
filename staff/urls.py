from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
	path('', views.index, name='index'),
	path('approve', views.approve, name='approve'),
	path('reject', views.reject, name='reject'),
	path('new', views.new, name='new'),
]