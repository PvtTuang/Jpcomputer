# Generated by Django 4.2.9 on 2024-05-10 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_order_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_items',
        ),
    ]