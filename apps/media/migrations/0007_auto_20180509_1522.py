# Generated by Django 2.0.1 on 2018-05-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20180508_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='souhu_app',
            name='resource_text',
            field=models.CharField(default='', max_length=1000, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='sina_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='爬取次数'),
        ),
        migrations.AlterField(
            model_name='souhu_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='爬取次数'),
        ),
        migrations.AlterField(
            model_name='toutiao_app',
            name='amount',
            field=models.IntegerField(default='1', verbose_name='爬取次数'),
        ),
    ]