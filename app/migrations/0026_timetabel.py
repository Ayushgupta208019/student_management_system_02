# Generated by Django 4.2.1 on 2023-08-05 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_hsotel_block_hosteldetails_hostel_block_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]
