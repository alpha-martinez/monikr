# Generated by Django 3.1.1 on 2020-09-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_delete_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='icon',
            field=models.CharField(default='upload icon', max_length=250),
        ),
    ]
