# Generated by Django 3.1.6 on 2021-04-21 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0031_auto_20210421_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 18, 59, 34, 674264), verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Cancel Reason (Only to be filled when order is cancelled)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Processing', 'Processing'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled')], default='Order Placed', max_length=50),
        ),
    ]
