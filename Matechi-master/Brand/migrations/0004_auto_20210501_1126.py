# Generated by Django 3.1.6 on 2021-05-01 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0003_auto_20210422_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'ordering': ('brand_priority',), 'verbose_name': 'Brands', 'verbose_name_plural': 'Brands'},
        ),
    ]
