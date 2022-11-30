from django.db import models

# Create your models here.
class Item(models.Model):
	itemid = models.AutoField(primary_key=True)
	categlory = models.CharField(max_length=128, default='Item')
	itemname = models.CharField(max_length=128)
	description = models.CharField(max_length=1024)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	email = models.EmailField()