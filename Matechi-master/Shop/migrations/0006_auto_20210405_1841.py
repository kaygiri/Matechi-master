# Generated by Django 3.1.6 on 2021-04-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20210405_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
