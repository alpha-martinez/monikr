# Generated by Django 3.1.1 on 2020-09-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_auto_20200930_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='disclaimer',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='salon',
            name='content',
            field=models.TextField(default='write it out here', max_length=1000),
        ),
        migrations.AlterField(
            model_name='textexhibit',
            name='content',
            field=models.TextField(default='write it out here', max_length=1000),
        ),
    ]
