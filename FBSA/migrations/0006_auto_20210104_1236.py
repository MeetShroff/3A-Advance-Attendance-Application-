# Generated by Django 3.1.4 on 2021-01-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0005_department_fregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_Registration',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=300)),
                ('semester', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('n_pass', models.CharField(max_length=50)),
                ('c_pass', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Fregistration',
        ),
    ]