import xadmin
from django.db import connection, transaction
from .models import sina_app, toutiao_app, souhu_app, toutiao_parameter, toutiao_ad_to_parameter, toutiao_param


class sinaAdmin(object):
    list_display = ['id', 'pos', 'img_show', 'url_show', 'articlePreload', 'commentStatus', 'create_time',
                    'update_time', 'amount']
    search_fields = ['pos', 'title', 'articlePreload', 'commentStatus', 'amount']
    list_filter = ['pos', 'title', 'articlePreload', 'commentStatus', 'create_time', 'update_time', 'amount']

    model_icon = 'fa fa-pie-chart'

    def has_add_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def has_delete_permission(request, obj=None):
        return False


xadmin.site.register(sina_app, sinaAdmin)


class toutiaoAdmin(object):
    list_display = ['id', 'img_show', 'url_show', 'read_count', 'share_count', 'source', 'create_time', 'update_time',
                    'amount']
    search_fields = ['title', 'read_count', 'share_count', 'source', 'amount']
    list_filter = ['title', 'read_count', 'share_count', 'source', 'create_time', 'update_time', 'amount']

    model_icon = 'fa fa-pie-chart'

    def has_add_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def has_delete_permission(request, obj=None):
        return False


xadmin.site.register(toutiao_app, toutiaoAdmin)


class souhuAdmin(object):
    list_display = ['id', 'img_show', 'title_show', 'adid', 'weight', 'size', 'create_time', 'update_time', 'amount']
    search_fields = ['weight', 'adid', 'size', 'amount']
    list_filter = ['weight', 'adid', 'size', 'create_time', 'update_time', 'amount']

    model_icon = 'fa fa-pie-chart'

    def has_add_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def has_delete_permission(request, obj=None):
        return False

    # def queryset(self):
    #     qs = souhu_app.objects.all()
    #     for a in  qs:
    #         a.resource =eval(a.resource)
    #         print(a.resource)
    #     return  qs


xadmin.site.register(souhu_app, souhuAdmin)


class toutiao_paramAdmin(object):
    list_display = ['img_show', 'url_show', 'read_count', 'share_count', 'source', 'analysis', 'analysis_count',
                    'device_platform', 'channel']
    search_fields = ['id']
    list_filter = ['id']

    def queryset(self):
        cursor = connection.cursor()
        cursor.execute(
            "select tp.id,tp.read_count, tp.share_count, tp.source from toutiao_app tp,toutiao_ad_to_parameter where tp.id = toutiao_ad_to_parameter.toutiao_ad_id")
        date = cursor.fetchall()
        return toutiao_param.objects.filter(id__in=[x[0] for x in date])

    # list_display = ['id','img_show','url_show','read_count','share_count','source','create_time','update_time','amount']
    # search_fields = ['title','read_count','share_count','source','amount']
    # list_filter = ['title','read_count','share_count','source','create_time','update_time','amount']
    #
    # model_icon = 'fa fa-pie-chart'

    # def queryset(self):
    #
    #     for i in toutiao_parameter.objects.filter(city='广州').values('id'):
    #         for j in toutiao_ad_to_parameter.objects.filter(toutiao_para_id=i['id']).values('toutiao_ad_id'):
    #             qs = toutiao_app.objects.filter(id=j['toutiao_ad_id'])
    #             print(qs)
    #
    #     return qs
    model_icon = 'fa fa-pie-chart'

    def has_add_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def has_delete_permission(request, obj=None):
        return False


xadmin.site.register(toutiao_param, toutiao_paramAdmin)
