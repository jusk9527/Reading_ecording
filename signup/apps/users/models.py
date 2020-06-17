from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名",help_text="菜单名")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标", help_text="图标")
    path = models.CharField(max_length=158, null=True, blank=True, verbose_name="链接地址", help_text="连接地址")
    is_frame = models.BooleanField(default=False, verbose_name="外部菜单", help_text="外部菜单")
    is_show = models.BooleanField(default=True, verbose_name="显示标记", help_text="显示标记")
    sort = models.IntegerField(null=True, blank=True, verbose_name="排序标记", help_text="排序标记")
    component = models.CharField(max_length=200, null=True, blank=True, verbose_name="组件", help_text="组件")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单", help_text="菜单层级")
    history = HistoricalRecords(excluded_fields=['add_time', 'modify_time'])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['id']




class Permission(models.Model):
    """
    权限
    """

    name = models.CharField(max_length=30, unique=True, verbose_name="权限名", help_text="权限")
    method = models.CharField(max_length=50, null=True, blank=True, verbose_name="方法", help_text="方法")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父权限", help_text="父权限")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']



class Organization(models.Model):
    """
    组织架构
    """
    organization_type_choices = (
        ("company", "公司"),
        ("department", "学校")
    )
    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=organization_type_choices, default="department", verbose_name="类型")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父类组织")
    sort = models.IntegerField(verbose_name="排序", null=True, blank=True,default=0)

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色", help_text="角色")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限", help_text="权限")
    menus = models.ManyToManyField("Menu", blank=True, verbose_name="菜单", help_text="菜单")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述", help_text="描述")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class UserProfile(AbstractUser):
    """
    用户
    """
    POSITION_CHOICES = (
        ("superuser", u"超级管理员"),
        ("Investor", u"投资人"),
        ("principal", u"校长"),
        ("grade_director",u"年级主任"),
        ("tearcher",u"老师"),
    )
    name = models.CharField("姓名",max_length=30, null=True, blank=True, help_text="姓名")
    mobile = models.CharField("电话",max_length=11,null=True, blank=True,help_text='手机号',)
    email = models.EmailField("邮箱",max_length=100, null=True, blank=True,help_text="邮箱")
    openid = models.CharField(verbose_name="微信ID", max_length=30, null=False, blank=False, help_text="微信的唯一标识符",default=0)
    session_key = models.CharField(verbose_name="微信的session_key", max_length=30, blank=False, help_text="微信的session_key", default=0)
    password = models.CharField(verbose_name="用户的密码",max_length=100, blank=False, help_text="微信的密码")


    # department = models.ForeignKey("Organization", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="部门")
    department = models.ManyToManyField("Organization", null=True, blank=True, verbose_name="学校",related_name="user_department")

    position = models.CharField(max_length=50,choices=POSITION_CHOICES, null=True, blank=True, verbose_name="职位")
    image = models.ImageField(upload_to="user/images/%Y/%m",default="user/default.png",max_length=100, null=True, blank=True)
    roles = models.ManyToManyField("Role", verbose_name="角色", blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username








