# Generated by Django 3.1.6 on 2021-04-22 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0032_auto_20210421_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 21, 20, 29, 813461), verbose_name='Created On'),
        ),
    ]
