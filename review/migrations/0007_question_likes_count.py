# Generated by Django 3.1 on 2020-09-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_question_likes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]