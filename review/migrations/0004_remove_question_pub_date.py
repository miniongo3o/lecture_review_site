# Generated by Django 3.1 on 2020-09-08 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20200825_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]