# Generated by Django 3.1.2 on 2021-09-21 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_sessionpartners'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SessionPartners',
            new_name='SessionPartner',
        ),
    ]
