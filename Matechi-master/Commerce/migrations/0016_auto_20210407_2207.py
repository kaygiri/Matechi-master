# Generated by Django 3.1.6 on 2021-04-07 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0015_auto_20210407_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 22, 7, 35, 11776), verbose_name='Created On'),
        ),
    ]