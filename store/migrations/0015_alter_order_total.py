# Generated by Django 4.0.3 on 2022-04-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
