# Generated by Django 4.2.9 on 2024-05-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_remove_product_has_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_detail',
            field=models.BooleanField(default=False),
        ),
    ]
