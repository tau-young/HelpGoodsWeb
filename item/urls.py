from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
	path('', views.index, name='index'),
	path('detail', views.detail, name='detail'),
	path('new', views.new, name='new'),
	path('edit', views.edit, name='edit'),
	path('delete', views.delete, name='delete'),
	path('categlory', views.categlories, name='categlories'),
	path('categlory/<str:cate>', views.categlory, name='categlory'),
]