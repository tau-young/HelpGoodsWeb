from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	email = models.EmailField(unique=True)

	@classmethod
	def create(self, username, address, phone, email):
		return self(username=username, address=address, phone=phone, email=email)