# Generated by Django 3.1.1 on 2020-09-25 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monikr', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('pronouns', models.CharField(max_length=50)),
                ('medium', models.CharField(max_length=50)),
                ('artist_statement', models.CharField(max_length=250)),
            ],
        ),
    ]
