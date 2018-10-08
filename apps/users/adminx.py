from django.contrib.auth.models import Permission, Group

import xadmin

# from sina.models import app
# from toutiao.models import app
from xadmin import views
from .models import UserProfile


# from .models import Banner,UserProfile,EmailVerifyRecord

# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']

    # 创建banner的管理类


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    pass


class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# 将model与admin管理器进行关联注册
# xadmin.site.register(Banner, BannerAdmin)
# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)


# 创建X admin的全局管理器并与view绑定。


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "ImageThinking"
    site_footer = "Copyright 2018,ImageThinking"
    # 收起菜单
    menu_style = "accordion"
    # def get_site_menu(self):
    #     from xadmin.models import Log
    #     return (
    #
    #         {'title': '系统管理', 'menus': (
    #             # {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
    #             {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
    #             {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
    #             {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
    #         )},
    #         {'title': '用户管理', 'menus': (
    #             {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
    #             # {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
    #         )},
    #         {'title': '流媒体', 'menus': (
    #             {'title': '新浪新闻app', 'url': self.get_model_url(sina.app, 'changelist')},
    #             {'title': '今日头条app', 'url': self.get_model_url(toutiao.app, 'changelist')},
    #             # {'title': '天天快报app', 'url': self.get_model_url(sina.app, 'changelist')},
    #             # {'title': 'wifi万能钥匙app', 'url': self.get_model_url(sina.app, 'changelist')},
    #             # {'title': '一点资讯app', 'url': self.get_model_url(sina.app, 'changelist')},
    #             # {'title': '新浪app', 'url': self.get_model_url(app, 'changelist')},
    #         )},)

    # 将头部与脚部信息进行注册:


xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(views.LoginView,
                     login_template="xadmin/views/xadmin_login.html"
                     )
