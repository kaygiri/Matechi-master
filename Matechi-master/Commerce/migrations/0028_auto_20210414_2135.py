# Generated by Django 3.1.6 on 2021-04-14 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0027_auto_20210414_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 21, 35, 52, 560332), verbose_name='Created On'),
        ),
    ]