# Generated by Django 3.0.5 on 2023-04-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20230422_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='semester_year',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.Semester_Year'),
        ),
    ]
