# Generated by Django 3.1.1 on 2020-09-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='tags',
            field=models.ManyToManyField(to='main_app.Tag'),
        ),
    ]
