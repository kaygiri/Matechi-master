# Generated by Django 3.1.6 on 2021-04-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_auto_20210408_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='int_average_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
