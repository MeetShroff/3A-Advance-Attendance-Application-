# Generated by Django 3.1.7 on 2021-04-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBSA', '0039_delete_f_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='subject',
        ),
    ]