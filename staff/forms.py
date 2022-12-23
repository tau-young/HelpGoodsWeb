from django import forms

class NewCategloryForm(forms.Form):
	name = forms.CharField(label='Categlory Name')
	attributes = forms.CharField(label='Attributes', widget=forms.Textarea, required=False)