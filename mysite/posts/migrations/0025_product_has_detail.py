# Generated by Django 4.2.9 on 2024-05-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_alter_computer_cpu_series_alter_notebook_cpu_series_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_detail',
            field=models.BooleanField(default=False),
        ),
    ]
