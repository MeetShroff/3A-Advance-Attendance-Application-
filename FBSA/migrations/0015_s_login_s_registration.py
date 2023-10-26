# Generated by Django 3.1.4 on 2021-02-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0014_auto_20210106_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_login',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('c_pass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='S_Registration',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_fname', models.CharField(max_length=50)),
                ('s_lname', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('e_no', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('b_date', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('n_pass', models.CharField(max_length=50)),
                ('c_pass', models.CharField(max_length=50)),
            ],
        ),
    ]