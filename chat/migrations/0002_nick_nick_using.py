# Generated by Django 3.1 on 2020-08-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nick',
            name='nick_using',
            field=models.BooleanField(default=False),
        ),
    ]
