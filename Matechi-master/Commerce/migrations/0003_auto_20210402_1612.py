# Generated by Django 3.1.6 on 2021-04-02 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0002_auto_20210402_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 16, 12, 37, 28713), verbose_name='Created On'),
        ),
    ]
