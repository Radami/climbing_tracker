# Generated by Django 3.0.7 on 2020-06-22 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20200622_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='climb',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.Session'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClimbingSession',
        ),
    ]
