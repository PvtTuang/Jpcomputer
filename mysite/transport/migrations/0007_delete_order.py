# Generated by Django 4.2.9 on 2024-05-09 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_remove_order_order_number_delete_slip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
