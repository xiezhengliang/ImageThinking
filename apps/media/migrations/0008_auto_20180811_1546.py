# Generated by Django 2.0.1 on 2018-08-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_auto_20180509_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(default='', max_length=64, verbose_name='media')),
                ('channel', models.CharField(default='', max_length=64, verbose_name='channel')),
                ('header', models.TextField(default='', verbose_name='header')),
                ('url', models.TextField(default='', verbose_name='url')),
                ('parameter', models.TextField(default='', verbose_name='parameter')),
                ('is_active', models.BooleanField(default='', verbose_name='is_active')),
                ('system', models.CharField(default='', max_length=50, verbose_name='system')),
            ],
            options={
                'verbose_name': '查询统计',
                'verbose_name_plural': '查询统计',
                'db_table': 'parameter',
            },
        ),
        migrations.CreateModel(
            name='toutiao_ad_to_parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toutiao_ad_id', models.IntegerField(default='1', verbose_name='toutiao_ad_id')),
                ('toutiao_para_id', models.IntegerField(default='1', verbose_name='toutiao_para_id')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '查询统计',
                'verbose_name_plural': '查询统计',
                'db_table': 'toutiao_ad_to_parameter',
            },
        ),
        migrations.CreateModel(
            name='toutiao_parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='', max_length=2000, verbose_name='header')),
                ('url', models.CharField(default='', max_length=200, verbose_name='url')),
                ('fp', models.CharField(default='', max_length=60, verbose_name='fp')),
                ('version_code', models.CharField(default='', max_length=60, verbose_name='version_code')),
                ('app_name', models.CharField(default='', max_length=60, verbose_name='app_name')),
                ('vid', models.CharField(default='', max_length=60, verbose_name='vid')),
                ('device_id', models.CharField(default='', max_length=60, verbose_name='device_id')),
                ('channel', models.CharField(default='', max_length=60, verbose_name='channel')),
                ('resolution', models.CharField(default='', max_length=60, verbose_name='resolution')),
                ('aid', models.CharField(default='', max_length=60, verbose_name='aid')),
                ('ab_version', models.CharField(default='', max_length=2000, verbose_name='ab_version')),
                ('ab_feature', models.CharField(default='', max_length=60, verbose_name='ab_feature')),
                ('ab_group', models.CharField(default='', max_length=60, verbose_name='ab_group')),
                ('openudid', models.CharField(default='', max_length=60, verbose_name='openudid')),
                ('idfv', models.CharField(default='', max_length=60, verbose_name='idfv')),
                ('ac', models.CharField(default='', max_length=60, verbose_name='ac')),
                ('os_version', models.CharField(default='', max_length=60, verbose_name='os_version')),
                ('ssmix', models.CharField(default='', max_length=60, verbose_name='ssmix')),
                ('device_platform', models.CharField(default='', max_length=60, verbose_name='device_platform')),
                ('iid', models.CharField(default='', max_length=60, verbose_name='iid')),
                ('ab_client', models.CharField(default='', max_length=60, verbose_name='ab_client')),
                ('device_type', models.CharField(default='', max_length=60, verbose_name='device_type')),
                ('idfa', models.CharField(default='', max_length=60, verbose_name='idfa')),
                ('refresh_reason', models.CharField(default='', max_length=60, verbose_name='refresh_reason')),
                ('detail', models.CharField(default='', max_length=60, verbose_name='detail')),
                ('last_refresh_sub_entrance_interval', models.CharField(default='', max_length=60, verbose_name='last_refresh_sub_entrance_interval')),
                ('tt_from', models.CharField(default='', max_length=60, verbose_name='tt_from')),
                ('count', models.CharField(default='', max_length=60, verbose_name='count')),
                ('list_count', models.CharField(default='', max_length=60, verbose_name='list_count')),
                ('support_rn', models.CharField(default='', max_length=60, verbose_name='support_rn')),
                ('LBS_status', models.CharField(default='', max_length=60, verbose_name='LBS_status')),
                ('cp', models.CharField(default='', max_length=60, verbose_name='cp')),
                ('loc_mode', models.CharField(default='', max_length=60, verbose_name='loc_mode')),
                ('min_behot_time', models.CharField(default='', max_length=60, verbose_name='min_behot_time')),
                ('session_refresh_idx', models.CharField(default='', max_length=60, verbose_name='session_refresh_idx')),
                ('image', models.CharField(default='', max_length=60, verbose_name='image')),
                ('strict', models.CharField(default='', max_length=60, verbose_name='strict')),
                ('refer', models.CharField(default='', max_length=60, verbose_name='refer')),
                ('city', models.CharField(default='', max_length=60, verbose_name='city')),
                ('concern_id', models.CharField(default='', max_length=60, verbose_name='concern_id')),
                ('language', models.CharField(default='', max_length=60, verbose_name='language')),
                ('st_time', models.CharField(default='', max_length=60, verbose_name='st_time')),
                ('_as', models.CharField(default='', max_length=60, verbose_name='_as')),
                ('ts', models.CharField(default='', max_length=60, verbose_name='ts')),
            ],
            options={
                'verbose_name': '查询统计',
                'verbose_name_plural': '查询统计',
                'db_table': 'toutiao_parameter',
            },
        ),
        migrations.AlterField(
            model_name='sina_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='发现次数'),
        ),
        migrations.AlterField(
            model_name='sina_app',
            name='pos',
            field=models.CharField(default='', max_length=500, verbose_name='pos'),
        ),
        migrations.AlterField(
            model_name='souhu_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='发现次数'),
        ),
        migrations.AlterField(
            model_name='souhu_app',
            name='special',
            field=models.TextField(default='', verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='toutiao_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='发现次数'),
        ),
    ]
