# Generated by Django 4.2.9 on 2024-05-20 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_product_has_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_detail',
        ),
    ]
