# Generated by Django 2.1.7 on 2019-03-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0008_auto_20190304_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='screen_control_type',
            field=models.IntegerField(
                choices=[(1, 'None'), (2, 'CEC RW'), (3, 'CEC RO'), (4, 'LG Serial'), (5, 'RPi TV Service')],
                default=1),
        ),
    ]
