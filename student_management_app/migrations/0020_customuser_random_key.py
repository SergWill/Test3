# Generated by Django 4.0.3 on 2022-05-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0019_remove_customuser_random_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='random_key',
            field=models.CharField(default=0, max_length=6),
        ),
    ]
