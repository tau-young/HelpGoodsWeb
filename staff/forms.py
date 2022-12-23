from django import forms

class NewCategoryForm(forms.Form):
	name = forms.CharField(label='Category Name')
	attributes = forms.CharField(label='Attributes', widget=forms.Textarea, required=False)