# Generated by Django 3.0.5 on 2023-04-21 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20230422_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_exam_result',
            old_name='subject_name',
            new_name='subject_id',
        ),
    ]
