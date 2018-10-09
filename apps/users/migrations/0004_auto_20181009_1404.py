# Generated by Django 2.0.1 on 2018-10-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_is_paying_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(default='', max_length=100, verbose_name='企业名称'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='principal',
            field=models.CharField(default='', max_length=10, verbose_name='负责人'),
        ),
    ]
