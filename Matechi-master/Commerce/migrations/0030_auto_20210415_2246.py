# Generated by Django 3.1.6 on 2021-04-15 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0029_auto_20210415_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 22, 46, 12, 86109), verbose_name='Created On'),
        ),
    ]
