# Generated by Django 4.0.4 on 2022-07-18 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_delivery_web', '0006_rename_order_id_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ID',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
