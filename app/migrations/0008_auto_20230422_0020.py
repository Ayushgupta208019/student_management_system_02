# Generated by Django 3.0.5 on 2023-04-21 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_document_file_student_exam_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_exam_result',
            old_name='subject_id',
            new_name='subject_name',
        ),
    ]