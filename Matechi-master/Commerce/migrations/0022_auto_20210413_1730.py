# Generated by Django 3.1.6 on 2021-04-13 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0021_auto_20210413_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 17, 30, 25, 53211), verbose_name='Created On'),
        ),
    ]