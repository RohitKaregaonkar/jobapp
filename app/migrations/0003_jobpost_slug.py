# Generated by Django 4.2.4 on 2023-09-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobpost_cretion_date_jobpost_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
