from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	# phone = PhoneNumberField()
	phone = models.CharField(max_length=128)
	email = models.EmailField(unique=True)

	@classmethod
	def create(self, username, password, address, phone, email):
		return self(username=username, password=password, address=address, phone=phone, email=email)