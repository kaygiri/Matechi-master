# Generated by Django 3.1.6 on 2021-05-03 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0040_auto_20210501_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 10, 57, 36, 713509), verbose_name='Created On'),
        ),
    ]