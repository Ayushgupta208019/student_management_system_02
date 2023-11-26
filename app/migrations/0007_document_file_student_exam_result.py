# Generated by Django 3.0.5 on 2023-04-21 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230418_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Exam_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_mark', models.IntegerField()),
                ('exam_marks', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Document_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='document/files')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subject')),
            ],
        ),
    ]