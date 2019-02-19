# Generated by Django 2.1.7 on 2019-02-18 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_content_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='contents')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.Content')),
            ],
        ),
    ]