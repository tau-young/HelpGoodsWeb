from django.db import models
from user.models import User

# Create your models here.
class Base(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=128, default='Item')
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=1024)
	publisher = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	email = models.EmailField()

	@classmethod
	def create(self, category, name, description, publisher, address, phone, email):
		return self(category=category, name=name, description=description, publisher=publisher, address=address, phone=phone, email=email)

class Item(Base):
	extra = models.JSONField(blank=True)