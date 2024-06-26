# Generated by Django 4.2.9 on 2024-04-30 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_printers_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectivitydevices',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connectivitydevice', to='posts.product'),
        ),
        migrations.AlterField(
            model_name='headphonespeakers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='headphonespeaker', to='posts.product'),
        ),
        migrations.AlterField(
            model_name='mousekeyboard',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mousekeyboard', to='posts.product'),
        ),
        migrations.AlterField(
            model_name='printers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printer', to='posts.product'),
        ),
        migrations.AlterField(
            model_name='sdcards_usbs',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sdcards_usb', to='posts.product'),
        ),
    ]
