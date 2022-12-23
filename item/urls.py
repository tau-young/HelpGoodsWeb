from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
	path('', views.index, name='index'),
	path('detail', views.detail, name='detail'),
	path('new', views.new, name='new'),
	path('new/<str:categlory>', views.new, name='new'),
	path('edit', views.edit, name='edit'),
	path('delete', views.delete, name='delete'),
	path('categlory', views.categlory, name='categlory'),
	path('categlory/<str:categlory>', views.categlory, name='categlory'),
]