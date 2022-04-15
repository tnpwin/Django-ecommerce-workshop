# Generated by Django 4.0.3 on 2022-03-30 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_carditem_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-created_on'], 'verbose_name': 'ตระกร้าสินค้า', 'verbose_name_plural': 'ข้อมูลตระกร้าสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='carditem',
            options={'verbose_name': 'ข้อมูลสินค้าในตระกร้า', 'verbose_name_plural': 'รายการสินค้าในตระกร้า'},
        ),
        migrations.RenameField(
            model_name='carditem',
            old_name='product_name',
            new_name='product',
        ),
    ]
