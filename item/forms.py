from django import forms
import inspect
from . import models

class NewItemForm(forms.ModelForm):
	class Meta:
		model = models.Base
		exclude = ['publisher']
		widgets = {
			'categlory': forms.HiddenInput()
		}