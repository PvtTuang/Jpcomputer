# Generated by Django 4.2.9 on 2024-05-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0011_remove_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='status',
            field=models.CharField(choices=[('อยู่ในตะกร้า', 'อยู่ในตะกร้า'), ('กำลังชำระเงิน', 'กำลังชำระเงิน'), ('ชำระเงินแล้ว', 'ชำระเงินแล้ว')], default='อยู่ในตะกร้า', max_length=20),
        ),
    ]
