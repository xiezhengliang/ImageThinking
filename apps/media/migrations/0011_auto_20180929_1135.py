# Generated by Django 2.0.1 on 2018-09-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0010_auto_20180813_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameter',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='id')),
                ('media', models.CharField(default='', max_length=64, null=True, verbose_name='media')),
                ('channel', models.CharField(default='', max_length=64, null=True, verbose_name='channel')),
                ('header', models.TextField(default='', null=True, verbose_name='header')),
                ('url', models.TextField(default='', null=True, verbose_name='url')),
                ('parameter', models.TextField(default='', null=True, verbose_name='parameter')),
                ('is_active', models.BooleanField(default='', verbose_name='is_active')),
                ('system', models.CharField(default='', max_length=50, null=True, verbose_name='system')),
            ],
            options={
                'verbose_name': '账户分析',
                'verbose_name_plural': '账户分析',
                'db_table': 'parameter',
            },
        ),
        migrations.DeleteModel(
            name='toutiao_param',
        ),
        migrations.CreateModel(
            name='toutiao_param',
            fields=[
            ],
            options={
                'verbose_name': '账户分析',
                'verbose_name_plural': '账户分析',
                'db_table': 'toutiao_param',
                'proxy': True,
                'indexes': [],
            },
            bases=('media.toutiao_app',),
        ),
    ]
