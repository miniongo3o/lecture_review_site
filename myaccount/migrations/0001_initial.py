# Generated by Django 3.0.5 on 2020-08-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('nickname', models.CharField(default='', max_length=10, unique=True, verbose_name='닉네임')),
                ('my_class', models.SmallIntegerField(blank=True, choices=[(0, 'MANAGER'), (1, 'AI'), (2, 'CLOUD'), (3, 'BIGDATA'), (4, 'IOT')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
