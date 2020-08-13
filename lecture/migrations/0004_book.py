# Generated by Django 3.1 on 2020-08-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20200810_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
