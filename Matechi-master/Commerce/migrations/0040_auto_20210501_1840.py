# Generated by Django 3.1.6 on 2021-05-01 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0039_auto_20210501_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 18, 40, 41, 674511), verbose_name='Created On'),
        ),
    ]