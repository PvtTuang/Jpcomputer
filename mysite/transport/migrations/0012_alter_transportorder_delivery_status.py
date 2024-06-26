# Generated by Django 4.2.9 on 2024-05-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0011_alter_transportorder_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportorder',
            name='delivery_status',
            field=models.CharField(choices=[('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งเสร็จสิ้น', 'จัดส่งเสร็จสิ้น'), ('ขอคืนสินค้า', 'ขอคืนสินค้า'), ('คืนสินค้าสำเร็จ', 'คืนสินค้าสำเร็จ')], default='กำลังจัดส่ง', max_length=100),
        ),
    ]
