# Generated by Django 3.1.6 on 2021-04-07 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0017_auto_20210407_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 22, 38, 34, 193406), verbose_name='Created On'),
        ),
    ]