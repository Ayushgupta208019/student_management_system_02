# Generated by Django 3.0.5 on 2023-04-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_notification',
            name='student_id',
        ),
    ]
