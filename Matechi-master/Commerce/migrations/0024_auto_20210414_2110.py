# Generated by Django 3.1.6 on 2021-04-14 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0023_auto_20210413_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 21, 10, 0, 752188), verbose_name='Created On'),
        ),
    ]