# Generated by Django 4.2.9 on 2024-04-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_connectivitydevices_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mousekeyboard',
            name='dpi',
            field=models.CharField(choices=[('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('6000', '6000'), ('7000', '7000'), ('8000', '8000'), ('9000', '9000'), ('10000', '10000')], max_length=50),
        ),
    ]
