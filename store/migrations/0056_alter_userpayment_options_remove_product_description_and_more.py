# Generated by Django 4.0.3 on 2022-04-14 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0055_alter_userpayment_method'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpayment',
            options={'verbose_name': 'การชำระเงิน', 'verbose_name_plural': 'ข้อมูลการชำระเงิน'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='diameter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lens',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thickness',
        ),
    ]