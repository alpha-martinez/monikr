# Generated by Django 3.1.1 on 2020-09-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_remebered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.observer'),
        ),
    ]
