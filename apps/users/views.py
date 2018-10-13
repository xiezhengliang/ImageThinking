from django.shortcuts import render

# Create your views here.
import random
import uuid
from dysms_python.demo_sms_send import send_sms
from users.models import UserProfile, VerifyCode
from django.http import HttpResponse
import json
import datetime
from datetime import timedelta
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth



def login(request):
    if request.method == "POST":
        mobile = request.POST.get('username', "")
        verification_code = request.POST.get('register_code', "")
        verify_records = VerifyCode.objects.filter(mobile=mobile).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            one_mintes_ago = datetime.datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
            if one_mintes_ago > last_record.add_time.replace(tzinfo=None):
                resp = {'respcode': 0, 'detail': '验证码已过期,请重新获取！'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            if last_record.code != verification_code:
                resp = {'respcode': 0, 'detail': '验证码错误'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            else:
                user = auth.authenticate(mobile=mobile)  # 用户验证
                if user:
                    login(request, user)  # 用户登录
                resp = {'respcode': 1, 'detail': '登录成功！'}
                return HttpResponse(json.dumps(resp), content_type="application/json")


def register(request):

    if request.method == "POST":
        company_name = request.POST.get("company_name")
        principal = request.POST.get("principal")
        mobile = request.POST.get("mobile")
        verification_code = request.POST.get('verification_code')
        verify_records = VerifyCode.objects.filter(mobile=mobile).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            one_mintes_ago = datetime.datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
            if one_mintes_ago > last_record.add_time.replace(tzinfo=None):
                resp = {'respcode': 0, 'detail': '验证码已过期,请重新获取！'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            if last_record.code != verification_code:
                resp = {'respcode': 0, 'detail': '验证码错误'}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            else:
                is_user_exist = UserProfile.objects.filter(username=mobile)
                if is_user_exist:
                    resp = {'respcode': 0, 'detail': '手机号已经注册'}
                    return HttpResponse(json.dumps(resp), content_type="application/json")
                else:
                    user = UserProfile.objects.create(company_name=company_name, username=mobile, principal=principal,
                                                      mobile=mobile)
                    user.save()
                    resp = {'respcode': 1, 'detail': '注册成功！'}
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
    verify_code = VerifyCode.objects.create(mobile=phone_number, code=code)
    verify_code.save()
    resp = {'respcode': 1, 'detail': code}
    return HttpResponse(json.dumps(resp), content_type="application/json")


class MobileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, mobile=None, **kwargs):
        # if mobile is None:
        if mobile is None:
            user = UserProfile.objects.get(username=username)
        else:
            try:
                user = UserProfile.objects.get(mobile=mobile)
            except UserProfile.DoesNotExist:
                return None
        if user.check_password(password):
            return user
