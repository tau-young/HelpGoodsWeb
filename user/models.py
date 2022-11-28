from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	contactInfo = models.CharField(max_length=128)

	def __str__(self):
		return self.username