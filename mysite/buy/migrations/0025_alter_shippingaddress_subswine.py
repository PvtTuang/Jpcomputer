# Generated by Django 4.2.9 on 2024-05-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0024_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='subswine',
            field=models.CharField(blank=True, default='-', max_length=100),
        ),
    ]