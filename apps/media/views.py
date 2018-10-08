from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from media.models import toutiao_app


class echart(View):
    def get(self, request):
        # print('dasfa')
        city_listname = ['广州', '深圳', '东莞', '佛山']
        # arr = [{"name": "name_1", "level": 1}, {"name": "name_2", "level": 0}, {"name": "name_3", "level": 3}]
        city_listcount = [
            {"value": 425, "name": '广州'},
            {"value": 309, "name": '深圳'},
            {"value": 254, "name": '东莞'},
            {"value": 235, "name": '佛山'},
        ]
        city_data = []
        for city in city_listname:
            city_data.append(toutiao_app.objects.filter(city=city).values('id').count())

        cursor = connection.cursor()
        cursor.execute(
            "select DATE_FORMAT(toutiao_app.create_time, '%Y-%m-%d') as tim ,count(*) as coun from toutiao_app group by DATE_FORMAT(toutiao_app.create_time, '%Y-%m-%d') ")
        # time_date = cursor.fetchall()
        time_date = []
        time_list = []
        for i in dictfetchall(cursor):
            time_date.append(i['coun'])
            time_list.append(i['tim'])
        # from django.db import connection, transaction
        # cursor = connection.cursor()
        #
        # # 数据修改操作——提交要求
        # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        # transaction.commit_unless_managed()
        #
        # # 数据检索操作,不需要提交
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])

        return JsonResponse({'city_list': city_listname, 'city_data': city_data, 'city_listcount': city_listcount,
                             'time_list': time_list, 'time_date': time_date})


def dictfetchall(cursor):
    """将游标返回的结果保存到一个字典对象中"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
