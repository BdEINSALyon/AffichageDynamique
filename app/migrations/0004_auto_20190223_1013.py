# Generated by Django 2.1.7 on 2019-02-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_screen_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='height',
        ),
        migrations.RemoveField(
            model_name='screen',
            name='width',
        ),
        migrations.AlterField(
            model_name='screen',
            name='date_last_call',
            field=models.DateTimeField(),
        ),
    ]
