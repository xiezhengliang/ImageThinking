from django.shortcuts import render

# Create your views here.
import random
import uuid
from dysms_python.demo_sms_send import send_sms
from users.models import UserProfile
from django.http import HttpResponse
import json
from django.contrib.auth import login

def login1(request):
    if request.method == "POST":
        print("登陆")
        pass

    pass

def register(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        principal = request.POST.get("principal")
        mobile = request.POST.get("mobile")
        username = company_name+str(uuid.uuid1())
        is_user_exist = UserProfile.objects.filter(username=mobile)
        if is_user_exist:
            resp = {'errorcode': 0, 'detail': '手机号已经注册'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            user = UserProfile.objects.create(company_name=company_name, username=mobile, principal=principal, mobile=mobile)
            user.save()
            login(request, is_user_exist)
            resp = {'errorcode': 1, 'detail': '注册成功！'}
            return HttpResponse(json.dumps(resp), content_type="application/json")

def send_message(request):
    # """发送信息的视图函数"""
    # 获取ajax的get方法发送过来的手机号码
    phone_number = request.GET.get('mobile')
    sign_name = "广东原昇"
    template_code = "SMS_143860075"
    l = []
    for i in range(6):
        rand_num = random.randint(0, 9)
        l.append(str(rand_num))
    code = ''.join(l)
    __business_id = uuid.uuid1()
    send_sms(__business_id, phone_number, sign_name, template_code, '{"code":"' + code + '"}')
    request.session['regist_code'] = code
    # return render(request, '')
    resp = {'respcode': 1, 'detail': code}
    return HttpResponse(json.dumps(resp), content_type="application/json")
