# Generated by Django 3.1.6 on 2021-04-07 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0010_auto_20210407_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.product'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]