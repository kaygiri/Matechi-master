# Generated by Django 3.1.6 on 2021-04-13 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0019_auto_20210408_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 17, 3, 5, 736796), verbose_name='Created On'),
        ),
    ]
