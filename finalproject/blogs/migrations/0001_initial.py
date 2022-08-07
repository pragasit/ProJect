# Generated by Django 4.0.2 on 2022-08-07 18:07

import blogs.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='Videos/%y', validators=[blogs.validators.file_size])),
            ],
        ),
    ]
