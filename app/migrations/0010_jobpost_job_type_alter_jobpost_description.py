# Generated by Django 4.2.4 on 2023-10-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_skills_jobpost_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship')], default='Full Time', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]