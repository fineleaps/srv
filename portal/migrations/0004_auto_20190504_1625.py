# Generated by Django 2.2.1 on 2019-05-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_survey_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
    ]