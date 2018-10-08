from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from django.db import connection, transaction

# from media.views import dictfetchall


class sina_app(models.Model):
    #
    pos = models.CharField(max_length=500, verbose_name=u"pos", default="")
    newsId = models.CharField(max_length=500, verbose_name=u"新闻id", default="")
    title = models.CharField(max_length=500, verbose_name=u"标题", default="")
    link = models.CharField(max_length=500, verbose_name=u"链接", default="")
    pic = models.CharField(max_length=500, verbose_name=u"图片url", default="")
    showTag = models.CharField(max_length=500, verbose_name=u"标识", default="")
    articlePreload = models.CharField(max_length=500, verbose_name=u"文章预加载", default="")
    commentStatus = models.CharField(max_length=500, verbose_name=u"评论状态", default="")
    adid = models.CharField(max_length=500, verbose_name=u"广告id", default="")
    dislikeTags = models.CharField(max_length=500, verbose_name=u"是否展示更多", default="")
    create_time = models.DateTimeField(verbose_name=u"创建时间", null=True, blank=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", null=True, blank=True)
    amount = models.IntegerField(verbose_name=u"发现次数", default="1")
    #url = models.CharField(verbose_name='sss',max_length=100,default='http://s3.pfp.sina.net/ea/ad/7/14/a04eba3148167a8e3127f4526bfd3387.jpg')
    # pic = models.ImageField(
    #     verbose_name='图片url',
    #     default=u"",
    #     max_length=500
    # )
    def img_show(self):
        file_url = self.pic
        return mark_safe('<img width=100px src="' + file_url + '"/>')

    def url_show(self):
        url = self.link
        return mark_safe('<a  href="' + url + '" target="_blank" />' + self.title + '</a>')


    img_show.short_description = "图片url"
    url_show.short_description = "标题"

    class Meta:
        verbose_name = u"新浪app"
        db_table = 'sina_app'
        verbose_name_plural = verbose_name

class toutiao_app(models.Model):
    #
    # share_url = models.CharField(max_length=1024, verbose_name=u"点击链接", default="")
    # display_info = models.CharField(max_length=500, verbose_name=u"展示消息", default="")
    # title = models.CharField(max_length=500, verbose_name=u"标题", default="")
    # display_url = models.CharField(max_length=500, verbose_name=u"点击链接", default="")
    # filter_words = models.CharField(max_length=500, verbose_name=u"", default="")
    # has_video = models.CharField(max_length=500, verbose_name=u"是否有视频", default="")
    # publish_time = models.CharField(max_length=500, verbose_name=u"发表时间戳", default="")
    # read_count = models.CharField(max_length=500, verbose_name=u"看过的次数", default="")
    # share_count = models.CharField(max_length=500, verbose_name=u"分享次数", default="")
    # show_more = models.CharField(max_length=500, verbose_name=u"是否展示更多", default="")
    # source = models.CharField(max_length=500, verbose_name=u"发布者名称", default="")
    # url = models.CharField(max_length=500, verbose_name=u"点击链接", default="")
    # repin_count = models.CharField(max_length=500, verbose_name=u"", default="")
    # label = models.CharField(max_length=500, verbose_name=u"标签", default="")
    # creat_time = models.DateField(verbose_name=u"创建时间", null=True, blank=True)
    title = models.CharField(max_length=500, verbose_name=u"标题", default="")
    city = models.CharField(max_length=20, verbose_name=u"城市", default="")
    source = models.CharField(max_length=50, verbose_name=u"广告来源", default="")
    display_url = models.CharField(max_length=1024, verbose_name=u"展示地址", default="")
    label = models.CharField(max_length=20, verbose_name=u"标签", default="")
    url = models.TextField(verbose_name=u"链接地址", default="")
    share_count = models.CharField(max_length=20, verbose_name=u"分享次数", default="")
    read_count = models.CharField(max_length=10, verbose_name=u"看过的次数", default="")
    publish_time = models.CharField(max_length=20, verbose_name=u"发表时间戳", default="")
    has_video = models.CharField(max_length=10, verbose_name=u"是否有视频", default="")
    create_time = models.DateTimeField(verbose_name=u"创建时间", null=True, blank=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", null=True, blank=True)
    amount = models.IntegerField( verbose_name=u"发现次数", default="1")
    abstract = models.CharField(max_length=50, verbose_name=u"abstract", default="")
    action_list = models.TextField(verbose_name=u"action_list", default="")
    aggr_type = models.CharField(max_length=64, verbose_name=u"aggr_type", default="")
    allow_download = models.CharField(max_length=10, verbose_name=u"allow_download", default="")
    article_sub_type = models.CharField(max_length=4, verbose_name=u"article_sub_type", default="")
    article_tpye = models.CharField(max_length=4, verbose_name=u"article_tpye", default="")
    article_url = models.TextField(verbose_name=u"article_url", default="")
    ban_comment = models.CharField(max_length=10, verbose_name=u"ban_comment", default="")
    behot_time = models.CharField(max_length=20, verbose_name=u"behot_time", default="")
    bury_count = models.CharField(max_length=20, verbose_name=u"bury_count", default="")
    cell_flag = models.CharField(max_length=20, verbose_name=u"cell_flag", default="")
    cell_layout_style = models.CharField(max_length=20, verbose_name=u"cell_layout_style", default="")
    cell_type = models.CharField(max_length=20, verbose_name=u"cell_type", default="")
    comment_count = models.CharField(max_length=20, verbose_name=u"comment_count", default="")
    content_decoration = models.CharField(max_length=20, verbose_name=u"content_decoration", default="")
    digg_count = models.CharField(max_length=20, verbose_name=u"digg_count", default="")
    filter_words = models.TextField(verbose_name=u"filter_words", default="")
    group_flags = models.CharField(max_length=20, verbose_name=u"group_flags", default="")
    group_id = models.CharField(max_length=50, verbose_name=u"group_id", default="")
    hot = models.CharField(max_length=10, verbose_name=u"hot", default="")
    ignore_web_transform = models.CharField(max_length=10, verbose_name=u"ignore_web_transform", default="")
    is_subject = models.CharField(max_length=20, verbose_name=u"is_subject", default="")
    item_id = models.CharField(max_length=50, verbose_name=u"item_id", default="")
    item_version = models.CharField(max_length=4, verbose_name=u"item_version", default="")
    label_style = models.CharField(max_length=4, verbose_name=u"label_style", default="")
    large_image_list = models.TextField(verbose_name=u"large_image_list", default="")
    level = models.CharField(max_length=4, verbose_name=u"level", default="")
    log_pb = models.TextField(verbose_name=u"log_pb", default="")
    natant_level = models.CharField(max_length=4, verbose_name=u"natant_level", default="")
    preload_web = models.CharField(max_length=4, verbose_name=u"preload_web", default="")
    raw_ad_data = models.TextField(verbose_name=u"raw_ad_data", default="")
    repin_count = models.CharField(max_length=10, verbose_name=u"repin_count", default="")
    rid = models.CharField(max_length=200, verbose_name=u"rid", default="")
    share_info = models.TextField(verbose_name=u"share_info", default="")
    share_url = models.TextField(verbose_name=u"share_url", default="")
    show_dislike = models.CharField(max_length=10, verbose_name=u"show_dislike", default="")
    show_portrait = models.CharField(max_length=10, verbose_name=u"show_portrait", default="")
    show_portrait_article = models.CharField(max_length=10, verbose_name=u"show_portrait_article", default="")
    source_avatar = models.CharField(max_length=100, verbose_name=u"source_avatar", default="")
    tag = models.CharField(max_length=10, verbose_name=u"tag", default="")
    tag_id = models.CharField(max_length=50, verbose_name=u"tag_id", default="")
    user_repin = models.CharField(max_length=10, verbose_name=u"user_repin", default="")
    user_verified = models.CharField(max_length=20, verbose_name=u"user_verified", default="")
    video_detail_info = models.TextField(verbose_name=u"video_detail_info", default="")
    video_duration = models.CharField(max_length=10, verbose_name=u"video_duration", default="")
    video_id = models.CharField(max_length=50, verbose_name=u"video_id", default="")
    video_play_info = models.TextField(verbose_name=u"video_play_info", default="")
    video_proportion_article = models.CharField(max_length=20, verbose_name=u"video_proportion_article", default="")
    video_style = models.CharField(max_length=10, verbose_name=u"video_style", default="")
    def url_show(self):
        if  self.share_url.strip():
            url = self.share_url
        else :
            url = '#'
        # nrl = none
        if self.title.strip():
            title = self.title
        else :
            title = '无'
        return mark_safe('<a  href="' + url + '" target="_blank" />' + title + '</a>')

    def img_show(self):
        # file_url = self.pic

        if not self.large_image_list.strip():
            file_url = self.large_image_list
        else :
            file_url = eval(self.large_image_list)[0]['url']
        # title = self.resource.title()
        return mark_safe('<img width=100px src="' + file_url + '"/>')

    img_show.short_description = "图片url"
    url_show.short_description = "标题"

    class Meta:
        verbose_name = u"今日头条app"
        db_table = 'toutiao_app'
        verbose_name_plural = verbose_name


class souhu_app(models.Model):
    adid = models.CharField(max_length=80, verbose_name=u"广告id", default="")
    resource_text = models.CharField(max_length=1000, verbose_name=u"标题", default="")
    special = models.TextField(verbose_name=u"备注", default="")
    create_time = models.DateTimeField(verbose_name=u"创建时间", null=True, blank=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", null=True, blank=True)
    amount = models.IntegerField(verbose_name=u"发现次数", default="1")
    monitorkey = models.CharField(max_length=50, verbose_name=u"monitorkey", default="")
    resource = models.TextField(verbose_name=u"resource", default="")
    resource2 = models.TextField(verbose_name=u"resource2", default="")
    weight = models.CharField(max_length=20, verbose_name=u"weight", default="")
    itemspaceid = models.CharField(max_length=20, verbose_name=u"itemspaceid", default="")
    resource1 = models.TextField(verbose_name=u"resource1", default="")
    impressionid = models.CharField(max_length=50, verbose_name=u"article_sub_type", default="")
    offline = models.CharField(max_length=80, verbose_name=u"offline", default="")
    viewmonitor = models.CharField(max_length=1000, verbose_name=u"viewmonitor", default="")
    size = models.CharField(max_length=20, verbose_name=u"size", default="")
    online = models.CharField(max_length=20, verbose_name=u"online", default="")
    position = models.CharField(max_length=20, verbose_name=u"position", default="")
    tag = models.CharField(max_length=20, verbose_name=u"tag", default="")
    editNews = models.CharField(max_length=10, verbose_name=u"editNews", default="")
    statsType = models.CharField(max_length=5, verbose_name=u"statsType", default="")
    isPreload = models.CharField(max_length=5, verbose_name=u"isPreload", default="")
    newsType = models.CharField(max_length=10, verbose_name=u"newsType", default="")
    gbcode = models.CharField(max_length=50, verbose_name=u"gbcode", default="")
    commentNum = models.CharField(max_length=10, verbose_name=u"commentNum", default="")
    isHasSponsorships = models.CharField(max_length=5, verbose_name=u"isHasSponsorships", default="")
    recomTime = models.CharField(max_length=5, verbose_name=u"recomTime", default="")
    newsId = models.CharField(max_length=30, verbose_name=u"newsId", default="")
    iconNight = models.TextField(verbose_name=u"iconNight", default="")
    isWeather = models.CharField(max_length=5, verbose_name=u"isWeather", default="")
    isRecom = models.CharField(max_length=5, verbose_name=u"isRecom", default="")
    iconText = models.CharField(max_length=10, verbose_name=u"iconText", default="")
    iconDay = models.TextField(verbose_name=u"iconDay", default="")
    link = models.TextField(verbose_name=u"link", default="")
    abposition = models.CharField(max_length=10, verbose_name=u"abposition", default="")
    adType = models.CharField(max_length=5, verbose_name=u"adType", default="")
    playTime = models.CharField(max_length=20, verbose_name=u"playTime", default="")
    adp_type = models.CharField(max_length=10, verbose_name=u"adp_type", default="")
    isFlash = models.CharField(max_length=5, verbose_name=u"isFlash", default="")
    isHasTv = models.CharField(max_length=5, verbose_name=u"isHasTv", default="")
    newschn = models.CharField(max_length=5, verbose_name=u"newschn", default="")



    def title_show(self):
        url = self.link
        return mark_safe('<a  href="' + url + '" target="_blank" />' + self.resource_text + '</a>')

    # def title_show(self):
    #     url = self.link
    #     if not self.resource.strip():
    #         title = self.resource
    #     else :
    #         title = eval(self.resource)['text']
    #     # title = self.resource.title()
    #     return mark_safe('<a  href="' + url + '" target="_blank" />' + title + '</a>')

    def img_show(self):
        # file_url = self.pic
        img_url = ""
        # if not self.resource1.strip():
        #     img_url = self.resource1
        # else :
        #     img_url = eval(self.resource1)['file']
        if "file" in eval(self.resource1):
            img_url = eval(self.resource1)['file']
        elif "file" in eval(self.resource):
            img_url = eval(self.resource)['file']
        elif "file" in eval(self.resource2):
            img_url = eval(self.resource2)['file']
        else:
            img_url = ""
        # title = self.resource.title()
        return mark_safe('<img width=100px src="' + img_url + '"/>')

    img_show.short_description = "图片url"
    title_show.short_description = "标题"

    class Meta:
        verbose_name = u"搜狐app"
        db_table = 'souhu_app'
        verbose_name_plural = verbose_name

class toutiao_parameter(models.Model):
    #
    header = models.TextField(verbose_name=u"header", default="",null=True)
    url = models.CharField(max_length=200, verbose_name=u"url", default="",null=True)
    fp = models.CharField(max_length=60, verbose_name=u"fp", default="",null=True)
    version_code = models.CharField(max_length=60, verbose_name=u"version_code", default="",null=True)
    app_name = models.CharField(max_length=60, verbose_name=u"app_name", default="",null=True)
    vid = models.CharField(max_length=60, verbose_name=u"vid", default="",null=True)
    device_id = models.CharField(max_length=60, verbose_name=u"device_id", default="",null=True)
    channel = models.CharField(max_length=60, verbose_name=u"channel", default="",null=True)
    resolution = models.CharField(max_length=60, verbose_name=u"resolution", default="",null=True)
    aid = models.CharField(max_length=60, verbose_name=u"aid", default="",null=True)
    ab_version = models.CharField(max_length=2000, verbose_name=u"ab_version", default="",null=True)
    ab_feature = models.CharField(max_length=60, verbose_name=u"ab_feature", default="",null=True)
    ab_group = models.CharField(max_length=60, verbose_name=u"ab_group", default="",null=True)
    openudid = models.CharField(max_length=60, verbose_name=u"openudid", default="",null=True)
    idfv = models.CharField(max_length=60, verbose_name=u"idfv", default="",null=True)
    ac = models.CharField(max_length=60, verbose_name=u"ac", default="",null=True)
    os_version = models.CharField(max_length=60, verbose_name=u"os_version", default="",null=True)
    ssmix = models.CharField(max_length=60, verbose_name=u"ssmix", default="",null=True)
    device_platform = models.CharField(max_length=60, verbose_name=u"device_platform", default="",null=True)
    iid = models.CharField(max_length=60, verbose_name=u"iid", default="",null=True)
    ab_client = models.CharField(max_length=60, verbose_name=u"ab_client", default="",null=True)
    device_type = models.CharField(max_length=60, verbose_name=u"device_type", default="",null=True)
    idfa = models.CharField(max_length=60, verbose_name=u"idfa", default="",null=True)
    refresh_reason = models.CharField(max_length=60, verbose_name=u"refresh_reason", default="",null=True)
    detail = models.CharField(max_length=60, verbose_name=u"detail", default="",null=True)
    last_refresh_sub_entrance_interval = models.CharField(max_length=60, verbose_name=u"last_refresh_sub_entrance_interval", default="",null=True)
    tt_from = models.CharField(max_length=60, verbose_name=u"tt_from", default="",null=True)
    count = models.CharField(max_length=60, verbose_name=u"count", default="",null=True)
    list_count = models.CharField(max_length=60, verbose_name=u"list_count", default="",null=True)
    support_rn = models.CharField(max_length=60, verbose_name=u"support_rn", default="",null=True)
    LBS_status = models.CharField(max_length=60, verbose_name=u"LBS_status", default="",null=True)
    cp = models.CharField(max_length=60, verbose_name=u"cp", default="",null=True)
    loc_mode = models.CharField(max_length=60, verbose_name=u"loc_mode", default="",null=True)
    min_behot_time = models.CharField(max_length=60, verbose_name=u"min_behot_time", default="",null=True)
    session_refresh_idx = models.CharField(max_length=60, verbose_name=u"session_refresh_idx", default="",null=True)
    image = models.CharField(max_length=60, verbose_name=u"image", default="",null=True)
    strict = models.CharField(max_length=60, verbose_name=u"strict", default="",null=True)
    refer = models.CharField(max_length=60, verbose_name=u"refer", default="",null=True)
    city = models.CharField(max_length=60, verbose_name=u"city", default="",null=True)
    concern_id = models.CharField(max_length=60, verbose_name=u"concern_id", default="",null=True)
    language = models.CharField(max_length=60, verbose_name=u"language", default="",null=True)
    st_time = models.CharField(max_length=60, verbose_name=u"st_time", default="",null=True)
    _as = models.CharField(max_length=60, verbose_name=u"_as", default="",null=True)
    ts = models.CharField(max_length=60, verbose_name=u"ts", default="",null=True)



    class Meta:
        verbose_name = u"账户分析"
        db_table = 'toutiao_parameter'
        verbose_name_plural = verbose_name

class toutiao_ad_to_parameter(models.Model):
    #
    toutiao_ad_id = models.IntegerField(verbose_name=u"toutiao_ad_id", default="1",null=True)
    toutiao_para_id = models.IntegerField(verbose_name=u"toutiao_para_id", default="1",null=True)
    time = models.DateTimeField(verbose_name=u"时间", null=True, blank=True)
    class Meta:
        verbose_name = u"账户分析"
        db_table = 'toutiao_ad_to_parameter'
        verbose_name_plural = verbose_name

class parameter(models.Model):
    #
    id = models.CharField(max_length=16, verbose_name='id', primary_key=True)
    media = models.CharField(max_length=64, verbose_name=u"media", default="",null=True)
    channel = models.CharField(max_length=64, verbose_name=u"channel", default="",null=True)

    header = models.TextField(verbose_name=u"header", default="",null=True)
    url = models.TextField(verbose_name=u"url", default="",null=True)
    parameter = models.TextField(verbose_name=u"parameter", default="",null=True)

    is_active = models.BooleanField(verbose_name=u"is_active", default="")
    system = models.CharField(max_length=50, verbose_name=u"system", default="",null=True)


    def getCity(self):
        cursor = connection.cursor()
        cursor.execute("SELECT city FROM toutiao_parameter GROUP BY city")
        city = cursor.fetchall()
        return city

    class Meta:
        verbose_name = u"账户分析"
        db_table = 'parameter'
        verbose_name_plural = verbose_name


class toutiao_param(toutiao_app):
    # title = models.CharField(max_length=500, verbose_name=u"标题", default="")
    # city = models.CharField(max_length=20, verbose_name=u"城市", default="")
    # source = models.CharField(max_length=50, verbose_name=u"广告来源", default="")
    # display_url = models.CharField(max_length=1024, verbose_name=u"展示地址", default="")
    # label = models.CharField(max_length=20, verbose_name=u"标签", default="")
    # url = models.TextField(verbose_name=u"链接地址", default="")
    # share_count = models.CharField(max_length=20, verbose_name=u"分享次数", default="")
    # read_count = models.CharField(max_length=10, verbose_name=u"看过的次数", default="")
    # publish_time = models.CharField(max_length=20, verbose_name=u"发表时间戳", default="")
    # has_video = models.CharField(max_length=10, verbose_name=u"是否有视频", default="")
    # create_time = models.DateTimeField(verbose_name=u"创建时间", null=True, blank=True)
    # update_time = models.DateTimeField(verbose_name=u"更新时间", null=True, blank=True)
    # amount = models.IntegerField( verbose_name=u"发现次数", default="1")
    # abstract = models.CharField(max_length=50, verbose_name=u"abstract", default="")
    # action_list = models.TextField(verbose_name=u"action_list", default="")
    # aggr_type = models.CharField(max_length=64, verbose_name=u"aggr_type", default="")
    # allow_download = models.CharField(max_length=10, verbose_name=u"allow_download", default="")
    # article_sub_type = models.CharField(max_length=4, verbose_name=u"article_sub_type", default="")
    # article_tpye = models.CharField(max_length=4, verbose_name=u"article_tpye", default="")
    # article_url = models.TextField(verbose_name=u"article_url", default="")
    # ban_comment = models.CharField(max_length=10, verbose_name=u"ban_comment", default="")
    # behot_time = models.CharField(max_length=20, verbose_name=u"behot_time", default="")
    # bury_count = models.CharField(max_length=20, verbose_name=u"bury_count", default="")
    # cell_flag = models.CharField(max_length=20, verbose_name=u"cell_flag", default="")
    # cell_layout_style = models.CharField(max_length=20, verbose_name=u"cell_layout_style", default="")
    # cell_type = models.CharField(max_length=20, verbose_name=u"cell_type", default="")
    # comment_count = models.CharField(max_length=20, verbose_name=u"comment_count", default="")
    # content_decoration = models.CharField(max_length=20, verbose_name=u"content_decoration", default="")
    # digg_count = models.CharField(max_length=20, verbose_name=u"digg_count", default="")
    # filter_words = models.TextField(verbose_name=u"filter_words", default="")
    # group_flags = models.CharField(max_length=20, verbose_name=u"group_flags", default="")
    # group_id = models.CharField(max_length=50, verbose_name=u"group_id", default="")
    # hot = models.CharField(max_length=10, verbose_name=u"hot", default="")
    # ignore_web_transform = models.CharField(max_length=10, verbose_name=u"ignore_web_transform", default="")
    # is_subject = models.CharField(max_length=20, verbose_name=u"is_subject", default="")
    # item_id = models.CharField(max_length=50, verbose_name=u"item_id", default="")
    # item_version = models.CharField(max_length=4, verbose_name=u"item_version", default="")
    # label_style = models.CharField(max_length=4, verbose_name=u"label_style", default="")
    # large_image_list = models.TextField(verbose_name=u"large_image_list", default="")
    # level = models.CharField(max_length=4, verbose_name=u"level", default="")
    # log_pb = models.TextField(verbose_name=u"log_pb", default="")
    # natant_level = models.CharField(max_length=4, verbose_name=u"natant_level", default="")
    # preload_web = models.CharField(max_length=4, verbose_name=u"preload_web", default="")
    # raw_ad_data = models.TextField(verbose_name=u"raw_ad_data", default="")
    # repin_count = models.CharField(max_length=10, verbose_name=u"repin_count", default="")
    # rid = models.CharField(max_length=200, verbose_name=u"rid", default="")
    # share_info = models.TextField(verbose_name=u"share_info", default="")
    # share_url = models.TextField(verbose_name=u"share_url", default="")
    # show_dislike = models.CharField(max_length=10, verbose_name=u"show_dislike", default="")
    # show_portrait = models.CharField(max_length=10, verbose_name=u"show_portrait", default="")
    # show_portrait_article = models.CharField(max_length=10, verbose_name=u"show_portrait_article", default="")
    # source_avatar = models.CharField(max_length=100, verbose_name=u"source_avatar", default="")
    # tag = models.CharField(max_length=10, verbose_name=u"tag", default="")
    # tag_id = models.CharField(max_length=50, verbose_name=u"tag_id", default="")
    # user_repin = models.CharField(max_length=10, verbose_name=u"user_repin", default="")
    # user_verified = models.CharField(max_length=20, verbose_name=u"user_verified", default="")
    # video_detail_info = models.TextField(verbose_name=u"video_detail_info", default="")
    # video_duration = models.CharField(max_length=10, verbose_name=u"video_duration", default="")
    # video_id = models.CharField(max_length=50, verbose_name=u"video_id", default="")
    # video_play_info = models.TextField(verbose_name=u"video_play_info", default="")
    # video_proportion_article = models.CharField(max_length=20, verbose_name=u"video_proportion_article", default="")
    # video_style = models.CharField(max_length=10, verbose_name=u"video_style", default="")




    def url_show(self):
        if  self.share_url.strip():
            url = self.share_url
        else :
            url = '#'
        # nrl = none
        if self.title.strip():
            title = self.title
        else :
            title = '无'
        return mark_safe('<a  href="' + url + '" target="_blank" />' + title + '</a>')

    def img_show(self):
        # file_url = self.pic

        if not self.large_image_list.strip():
            file_url = self.large_image_list
        else :
            file_url = eval(self.large_image_list)[0]['url']
        # title = self.resource.title()
        return mark_safe('<img width=100px src="' + file_url + '"/>')

    def analysis(self):
        cursor = connection.cursor()
        cursor.execute("select a.city,count(*) as cout from (select  tp.id,tpt.city from toutiao_app tp,toutiao_ad_to_parameter tatp,toutiao_parameter tpt where tp.id = tatp.toutiao_ad_id and tatp.toutiao_para_id = tpt.id)a where a.id = %s GROUP BY a.city",[self.id])
        # city = dictfetchall(cursor)
        desc = cursor.description
        list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
        string = ''
        for i in list :
            # string = string + i['city'] + ':' + str(i['cout']) + '    '
            if  i['city'].strip():
                string = string + i['city'] + '    '
        # for i in city:
        #     cursor1 = connection.cursor()
        #     cursor1.execute("SELECT city FROM toutiao_parameter GROUP BY city")
        # city = cursor.fetchall()
        return mark_safe(string)

    def analysis_count(self):
        cursor = connection.cursor()
        cursor.execute("select count(*) as cout from (select  tp.id,tpt.city from toutiao_app tp,toutiao_ad_to_parameter tatp,toutiao_parameter tpt where tp.id = tatp.toutiao_ad_id and tatp.toutiao_para_id = tpt.id)a where a.id = %s ",[self.id])
        # city = dictfetchall(cursor)
        desc = cursor.description
        list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
        count = 0
        for i in list :
            # string = string + i['city'] + ':' + str(i['cout']) + '    '
            # string = string + i['city'] + '    '
            count = count + i['cout']
        return mark_safe(str(count))

    def device_platform(self):
        cursor = connection.cursor()
        cursor.execute("select a.device_platform  from (select  tp.id,tpt.device_platform from toutiao_app tp,toutiao_ad_to_parameter tatp,toutiao_parameter tpt where tp.id = tatp.toutiao_ad_id and tatp.toutiao_para_id = tpt.id)a where a.id = %s GROUP BY a.device_platform",[self.id])
        # city = dictfetchall(cursor)
        desc = cursor.description
        list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
        string = ''
        for i in list :
            # string = string + i['city'] + ':' + str(i['cout']) + '    '
            string = string + i['device_platform'] + '    '
        return mark_safe(string)


    def channel(self):
        cursor = connection.cursor()
        cursor.execute("select a.channel  from (select  tp.id,tpt.channel from toutiao_app tp,toutiao_ad_to_parameter tatp,toutiao_parameter tpt where tp.id = tatp.toutiao_ad_id and tatp.toutiao_para_id = tpt.id)a where a.id = %s GROUP BY a.channel",[self.id])
        # city = dictfetchall(cursor)
        desc = cursor.description
        list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
        string = ''
        for i in list :
            # string = string + i['city'] + ':' + str(i['cout']) + '    '
            if i['channel'] == 'App%20Store':
                string = string + '苹果' + '    '
            else:
                string = string + i['channel'] + '    '
        return mark_safe(string)

    analysis_count.short_description = "发现天数"
    analysis.short_description = "投放地区"
    device_platform.short_description = "设备平台"
    channel.short_description = "channel"

    img_show.short_description = "图片url"
    url_show.short_description = "标题"

    class Meta:
        proxy = True
        verbose_name = u"账户分析"
        db_table = 'toutiao_param'
        verbose_name_plural = verbose_name