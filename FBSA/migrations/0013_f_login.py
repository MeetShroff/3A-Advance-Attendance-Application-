# Generated by Django 3.1.4 on 2021-01-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0012_auto_20210105_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_login',
            fields=[
                ('fl_id', models.AutoField(primary_key=True, serialize=False)),
                ('loginemail', models.CharField(max_length=50)),
                ('loginpass', models.CharField(max_length=100)),
            ],
        ),
    ]