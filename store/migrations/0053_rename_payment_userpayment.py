# Generated by Django 4.0.3 on 2022-04-13 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0052_alter_payment_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='UserPayment',
        ),
    ]
