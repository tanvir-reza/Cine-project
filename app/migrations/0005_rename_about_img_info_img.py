# Generated by Django 4.2.5 on 2023-09-28 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_info_about_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='about_img',
            new_name='img',
        ),
    ]
