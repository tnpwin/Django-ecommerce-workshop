# Generated by Django 4.0.3 on 2022-03-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_card_options_alter_carditem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carditem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]