# Generated by Django 4.0.3 on 2022-04-01 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_orderitem_color_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
