# Generated by Django 2.2.1 on 2019-05-04 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='slug',
        ),
    ]