# Generated by Django 4.0.3 on 2022-04-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', null=True, upload_to='avatar'),
        ),
    ]
