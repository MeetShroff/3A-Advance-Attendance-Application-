# Generated by Django 3.1.4 on 2021-03-31 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0034_auto_20210331_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='Semester',
        ),
    ]
