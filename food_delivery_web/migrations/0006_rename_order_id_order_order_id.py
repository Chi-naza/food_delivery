# Generated by Django 4.0.4 on 2022-07-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery_web', '0005_cartitem_user_order_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='order_ID',
        ),
    ]
