# Generated by Django 4.0.3 on 2022-05-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0013_subjects_oe_semester_id_subjects_oe_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects_oe',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subjects_oe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
