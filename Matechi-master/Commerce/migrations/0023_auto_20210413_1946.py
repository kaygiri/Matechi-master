# Generated by Django 3.1.6 on 2021-04-13 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0022_auto_20210413_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 19, 46, 51, 873434), verbose_name='Created On'),
        ),
    ]