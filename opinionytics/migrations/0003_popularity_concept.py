# Generated by Django 2.1.dev20180503070829 on 2018-05-21 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opinionytics', '0002_remove_popularity_concept'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularity',
            name='concept',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
