# Generated by Django 2.2.1 on 2019-05-04 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('headline', models.CharField(max_length=128)),
                ('purpose', models.TextField()),
                ('instructions', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=64)),
                ('serial_number', models.PositiveSmallIntegerField(default=30)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=32)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=32, unique=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.Question')),
            ],
        ),
    ]
