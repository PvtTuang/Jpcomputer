# Generated by Django 4.2.9 on 2024-04-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_mousekeyboard_dpi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='connectivitydevices',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='headphonespeakers',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='mousekeyboard',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='printers',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='sdcards_usbs',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='description',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='name',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='price',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='connectivitydevices',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='description',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='price',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='headphonespeakers',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='price',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='name',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='price',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='mousekeyboard',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='description',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='name',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='price',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='wwarranty',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='description',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='price',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='printers',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sdcards_usbs',
            name='warranty',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to='static/product_images/computer/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='static/product_images/computer/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='static/product_images/computer/'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(choices=[('1สัปดาห์', '1สัปดาห์'), ('2สัปดาห์', '2สัปดาห์'), ('3สัปดาห์', '3สัปดาห์'), ('1เดือน', '1เดือน'), ('2เดือน', '2เดือน'), ('3เดือน', '3เดือน'), ('4เดือน', '4เดือน'), ('5เดือน', '5เดือน'), ('6เดือน', '6เดือน')], max_length=8, null=True),
        ),
    ]