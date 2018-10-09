from django.shortcuts import render

# Create your views here.
import random
import uuid
from dysms_python.demo_sms_send import send_sms

def login(request):
    if request.method == "POST":
        print("登陆")
        pass

    pass

def register(request):
    pass


# 请求的路径
host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名（例如：cf_demo123）
account = "C44****38"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "ddd**************30 "

# def send_message(request):
#     """发送信息的视图函数"""
#     # 获取ajax的get方法发送过来的手机号码
#     mobile = request.GET.get('mobile')
#     # 通过手机去查找用户是否已经注册
#     user = UserProfile.objects.filter(uphone=mobile)
#     if len(user) == 1:
#         return JsonResponse({'msg': "该手机已经注册"})
#     # 定义一个字符串,存储生成的6位数验证码
#     message_code = ''
#     for i in range(6):
#         i = random.randint(0, 9)
#         message_code += str(i)
#     # 拼接成发出的短信
#     text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
#     # 把请求参数编码
#     params = urllib.parse.urlencode(
#         {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
#     # 请求头
#     headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#     # 通过全局的host去连接服务器
#     conn = http.client.HTTPConnection(host, port=80, timeout=30)
#     # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
#     conn.request("POST", sms_send_uri, params, headers)
#     # 得到服务器的响应
#     response = conn.getresponse()
#     # 获取响应的数据
#     response_str = response.read()
#     # 关闭连接
#     conn.close()
#     # 把验证码放进session中
#     request.session['message_code'] = message_code
#     print(eval(response_str.decode()))
#     # 使用eval把字符串转为json数据返回
#     return JsonResponse(eval(response_str.decode()))
#
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
