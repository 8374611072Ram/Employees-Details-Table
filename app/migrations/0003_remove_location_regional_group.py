# Generated by Django 4.1.1 on 2022-11-01 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_department_employee_department_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='regional_group',
        ),
    ]
