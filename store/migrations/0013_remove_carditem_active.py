# Generated by Django 4.0.3 on 2022-03-30 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_carditem_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carditem',
            name='active',
        ),
    ]