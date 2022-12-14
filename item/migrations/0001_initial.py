# Generated by Django 4.1.4 on 2022-12-23 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Base',
			fields=[
				('id', models.AutoField(primary_key=True, serialize=False)),
				('category', models.CharField(default='Item', max_length=128)),
				('name', models.CharField(max_length=128)),
				('description', models.CharField(max_length=1024)),
				('publisher', models.CharField(max_length=128)),
				('address', models.CharField(max_length=128)),
				('phone', models.CharField(max_length=128)),
				('email', models.EmailField(max_length=254)),
			],
		),
		migrations.CreateModel(
			name='Item',
			fields=[
				('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='item.base')),
				('extra', models.JSONField(blank=True)),
			],
			bases=('item.base',),
		),
	]
