# Generated by Django 3.1.6 on 2021-04-02 10:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('discount', models.IntegerField(verbose_name='Discount in percentage')),
                ('minimum_expense', models.IntegerField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2021, 4, 2, 16, 3, 7, 792839), verbose_name='Created On')),
                ('valid_until', models.DateTimeField(verbose_name='Valid Until')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('minimum_expense', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=100)),
                ('subtotal_price', models.PositiveBigIntegerField()),
                ('Coupon_used', models.CharField(blank=True, max_length=100, null=True, verbose_name='Coupon Code Used')),
                ('discount_amount', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Discount Amount')),
                ('delivery_charge', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Delivery Charge')),
                ('total_paid_price', models.PositiveBigIntegerField()),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Processing', 'Processing'), ('Packed', 'Packed'), ('Shipped', 'Shipped')], default='Paid', max_length=50)),
                ('complete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('province', models.CharField(choices=[('Province No. 1', 'Province No. 1'), ('Province No. 2', 'Province No. 2'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], max_length=100)),
                ('phone', models.BigIntegerField()),
                ('alternative_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('pickup_address', models.TextField()),
                ('special_notes', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commerce.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('province', models.CharField(choices=[('Province No. 1', 'Province No. 1'), ('Province No. 2', 'Province No. 2'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], max_length=100)),
                ('phone', models.BigIntegerField()),
                ('customer_pan_number', models.BigIntegerField(blank=True, null=True)),
                ('alternative_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('province', models.CharField(choices=[('Province No. 1', 'Province No. 1'), ('Province No. 2', 'Province No. 2'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], max_length=100)),
                ('phone', models.BigIntegerField()),
                ('customer_pan_number', models.BigIntegerField(blank=True, null=True)),
                ('alternative_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commerce.order')),
            ],
        ),
    ]
