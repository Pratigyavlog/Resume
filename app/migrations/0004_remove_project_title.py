# Generated by Django 4.2.7 on 2023-11-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_project_title_alter_project_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
    ]
