# Generated by Django 4.0.3 on 2022-04-10 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]