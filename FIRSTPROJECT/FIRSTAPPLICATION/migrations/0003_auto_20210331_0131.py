# Generated by Django 3.1.7 on 2021-03-31 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0002_student_technology'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='session1',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='technology',
            old_name='session1',
            new_name='session',
        ),
    ]
