from django.db import models
from django.contrib import admin
from user.models import User
from item.models import Base

# Create your models here.
class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	attributes = models.JSONField(blank=True)

	@classmethod
	def create(self, name, attributes):
		return self(name=name, attributes=attributes)