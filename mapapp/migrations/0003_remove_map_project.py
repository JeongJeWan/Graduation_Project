# Generated by Django 4.0.2 on 2022-03-31 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0002_map_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='project',
        ),
    ]