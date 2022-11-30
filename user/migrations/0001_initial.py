# Generated by Django 4.1.3 on 2022-11-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
