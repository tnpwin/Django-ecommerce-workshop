# Generated by Django 4.0.3 on 2022-04-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('method', models.CharField(choices=[('KTB', 'KTB'), ('K-BANK', 'K-BANK')], max_length=50)),
                ('datetime', models.DateField()),
            ],
        ),
    ]
