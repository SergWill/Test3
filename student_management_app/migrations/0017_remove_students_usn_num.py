# Generated by Django 4.0.3 on 2022-05-22 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0016_students_usn_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='usn_num',
        ),
    ]