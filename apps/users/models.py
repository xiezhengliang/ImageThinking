from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    # GENDER_CHOICES = (
    #     ("male", u"男"),
    #     ("female", u"女")
    # )
    # 昵称
    # nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # 生日，可以为空
    # birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    # gender = models.CharField(
    #     max_length=6,
    #     verbose_name=u"性别",
    #     choices=GENDER_CHOICES,
    #     default="female")
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    company_name = models.CharField(max_length=100, verbose_name="企业名称", default="")
    principal = models.CharField(max_length=10, verbose_name="负责人", default="")
    mobile = models.CharField(max_length=11, null=True, verbose_name="手机号", blank=True)
    is_paying_user = models.BooleanField(default=False)
    # # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100
    )


    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载Unicode方法，打印实例会打印username，username为继承自abstractuser
    def __unicode__(self):
        return self.username

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
