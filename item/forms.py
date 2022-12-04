from django import forms
import inspect
from . import models

class NewItemForm(forms.Form):
	categlory = forms.ChoiceField(label='Categlory', choices=[(cate, cate) for cate, _ in inspect.getmembers(models, inspect.isclass) if not cate in ['Base', 'User']])
	name = forms.CharField(label='Item Name')
	description = forms.CharField(label='Desciption')
	address = forms.CharField(label='Address')
	phone = forms.CharField(label='Phone')
	email = forms.EmailField()