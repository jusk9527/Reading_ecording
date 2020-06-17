from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model



# Create your models here.


User = get_user_model()
class ProList(models.Model):
    """
    问题列表
    """
    pro_title = models.TextField(verbose_name="问题标题", max_length=100,null=True,blank=True, default=0, help_text="问题标题")
    pro_brief = models.TextField(verbose_name="回答简短描述", max_length=100, help_text="问题简短描述")
    pro_desc = models.TextField(verbose_name=u"内容",  default='')

    class Meta:
        verbose_name = "问题列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pro_title)


class LoginLogs(models.Model):
    """
    登录日志
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户",max_length=100, help_text="用户")
    content = models.CharField(verbose_name="操作类型", null=True, blank=True,max_length=100,default="登录", help_text="登录")
    # IP = models.IPAddressField(verbose_name="操作IP", null=True, blank=True,default="")
    action_time = models.DateTimeField(verbose_name="操作时间", null=True,blank=True,max_length=100,default=datetime.now, help_text="操作时间")
    pass


class OperationLogs(models.Model):
    """
    ORM执行日志
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户",max_length=100, help_text="用户")
    type = models.CharField(verbose_name="类型",null=True, blank=True,default="successful",max_length=100, help_text="类型")
    content = models.CharField(verbose_name="修改详情", null=True, blank=True,default="无修改",max_length=100, help_text="修改详情")
    action_time = models.DateTimeField(verbose_name="操作时间", null=True,blank=True,default=datetime.now, help_text="操作时间")

