# Generated by Django 4.0.3 on 2022-03-29 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_card_alter_product_updated_on_carditem'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='card',
            table='Card',
        ),
        migrations.AlterModelTable(
            name='carditem',
            table='CardItem',
        ),
    ]
