# Generated by Django 2.0.1 on 2018-10-11 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181009_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='code',
            field=models.CharField(default='', max_length=10, verbose_name='验证码'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='code_add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
    ]
