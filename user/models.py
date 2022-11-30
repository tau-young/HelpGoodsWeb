from django.db import models
from enum import Enum

# Create your models here.
class UserType(Enum):
	Administrator = -1
	Unregistered = 0
	Unapproved = 1
	Regular = 2
	Locked = 3
	OtherException = 4

class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	email = models.EmailField(unique=True)
	usertype = models.IntegerField()

	@classmethod
	def create(self, username, address, phone, email):
		return self(username=username, address=address, phone=phone, email=email, usertype=UserType.Unapproved.value)