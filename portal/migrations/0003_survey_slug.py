# Generated by Django 2.2.1 on 2019-05-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_remove_survey_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]
