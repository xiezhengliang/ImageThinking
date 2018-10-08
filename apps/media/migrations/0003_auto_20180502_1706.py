# Generated by Django 2.0.1 on 2018-05-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20180502_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='toutiao_app',
            name='aggr_type',
            field=models.CharField(default='', max_length=64, verbose_name='aggr_type'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='allow_download',
            field=models.CharField(default='', max_length=10, verbose_name='allow_download'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='article_sub_type',
            field=models.CharField(default='', max_length=4, verbose_name='article_sub_type'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='article_tpye',
            field=models.CharField(default='', max_length=4, verbose_name='article_tpye'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='article_url',
            field=models.TextField(default='', verbose_name='article_url'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='ban_comment',
            field=models.CharField(default='', max_length=10, verbose_name='ban_comment'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='behot_time',
            field=models.CharField(default='', max_length=20, verbose_name='behot_time'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='bury_count',
            field=models.CharField(default='', max_length=20, verbose_name='bury_count'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='cell_flag',
            field=models.CharField(default='', max_length=20, verbose_name='cell_flag'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='cell_layout_style',
            field=models.CharField(default='', max_length=20, verbose_name='cell_layout_style'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='cell_type',
            field=models.CharField(default='', max_length=20, verbose_name='cell_type'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='comment_count',
            field=models.CharField(default='', max_length=20, verbose_name='comment_count'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='content_decoration',
            field=models.CharField(default='', max_length=20, verbose_name='content_decoration'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='creat_time',
            field=models.DateField(blank=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='digg_count',
            field=models.CharField(default='', max_length=20, verbose_name='digg_count'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='display_url',
            field=models.CharField(default='', max_length=1024, verbose_name='展示地址'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='filter_words',
            field=models.TextField(default='', verbose_name='filter_words'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='group_flags',
            field=models.CharField(default='', max_length=20, verbose_name='group_flags'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='group_id',
            field=models.CharField(default='', max_length=50, verbose_name='group_id'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='has_video',
            field=models.CharField(default='', max_length=10, verbose_name='是否有视频'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='hot',
            field=models.CharField(default='', max_length=10, verbose_name='hot'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='ignore_web_transform',
            field=models.CharField(default='', max_length=10, verbose_name='ignore_web_transform'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='is_subject',
            field=models.CharField(default='', max_length=20, verbose_name='is_subject'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='item_id',
            field=models.CharField(default='', max_length=50, verbose_name='item_id'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='item_version',
            field=models.CharField(default='', max_length=4, verbose_name='item_version'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='label',
            field=models.CharField(default='', max_length=20, verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='label_style',
            field=models.CharField(default='', max_length=4, verbose_name='label_style'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='large_image_list',
            field=models.TextField(default='', verbose_name='large_image_list'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='level',
            field=models.CharField(default='', max_length=4, verbose_name='level'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='log_pb',
            field=models.TextField(default='', verbose_name='log_pb'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='natant_level',
            field=models.CharField(default='', max_length=4, verbose_name='natant_level'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='preload_web',
            field=models.CharField(default='', max_length=4, verbose_name='preload_web'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='publish_time',
            field=models.CharField(default='', max_length=20, verbose_name='发表时间戳'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='raw_ad_data',
            field=models.TextField(default='', verbose_name='raw_ad_data'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='read_count',
            field=models.CharField(default='', max_length=10, verbose_name='看过的次数'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='repin_count',
            field=models.CharField(default='', max_length=10, verbose_name='repin_count'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='rid',
            field=models.CharField(default='', max_length=200, verbose_name='rid'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='share_count',
            field=models.CharField(default='', max_length=20, verbose_name='分享次数'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='share_info',
            field=models.TextField(default='', verbose_name='share_info'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='share_url',
            field=models.TextField(default='', verbose_name='share_url'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='show_dislike',
            field=models.CharField(default='', max_length=10, verbose_name='show_dislike'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='show_portrait',
            field=models.CharField(default='', max_length=10, verbose_name='show_portrait'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='show_portrait_article',
            field=models.CharField(default='', max_length=10, verbose_name='show_portrait_article'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='source',
            field=models.CharField(default='', max_length=50, verbose_name='广告来源'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='source_avatar',
            field=models.CharField(default='', max_length=100, verbose_name='source_avatar'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='tag_id',
            field=models.CharField(default='', max_length=50, verbose_name='tag_id'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='title',
            field=models.CharField(default='', max_length=500, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='url',
            field=models.TextField(default='', verbose_name='链接地址'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='user_repin',
            field=models.CharField(default='', max_length=10, verbose_name='user_repin'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='user_verified',
            field=models.CharField(default='', max_length=20, verbose_name='user_verified'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_detail_info',
            field=models.TextField(default='', verbose_name='video_detail_info'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_duration',
            field=models.CharField(default='', max_length=10, verbose_name='video_duration'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_id',
            field=models.CharField(default='', max_length=50, verbose_name='video_id'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_play_info',
            field=models.TextField(default='', verbose_name='video_play_info'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_proportion_article',
            field=models.CharField(default='', max_length=20, verbose_name='video_proportion_article'),
        ),
        migrations.AddField(
            model_name='toutiao_app',
            name='video_style',
            field=models.CharField(default='', max_length=10, verbose_name='video_style'),
        ),
        migrations.AlterField(
            model_name='toutiao_app',
            name='abstract',
            field=models.CharField(default='', max_length=50, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='toutiao_app',
            name='action_list',
            field=models.TextField(default='', verbose_name='action_list'),
        ),
    ]
