# Generated by Django 3.1.6 on 2021-04-21 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'ordering': ('brand_priority',)},
        ),
    ]
