# Generated by Django 4.0.3 on 2022-04-04 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_profileuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='user_image',
            field=models.ImageField(blank=True, default='user_default.png', null=True, upload_to='image_user'),
        ),
    ]
