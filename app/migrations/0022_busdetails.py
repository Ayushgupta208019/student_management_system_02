# Generated by Django 4.2.1 on 2023-07-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_student_enr'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_code', models.CharField(max_length=50)),
                ('bus_route', models.TextField()),
                ('bus_fair', models.IntegerField()),
                ('bus_type', models.CharField(max_length=50)),
            ],
        ),
    ]
