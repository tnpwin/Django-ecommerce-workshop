# Generated by Django 4.0.3 on 2022-04-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_order_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatar'),
        ),
    ]
