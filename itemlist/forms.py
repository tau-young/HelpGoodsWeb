from django import forms

class NewItemForm(forms.Form):
	categlory = forms.CharField(label='Categlory')
	itemname = forms.CharField(label='Item Name')
	description = forms.CharField(label='Desciption')
	address = forms.CharField(label='Address')
	phone = forms.CharField(label='Phone')
	email = forms.EmailField()

	@classmethod
	def create(self, user):
		return self('Item', '', '', user.address, user.phone, user.email)