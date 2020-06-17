# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     permission
   Description :
   Author :       jusk?
   date：          2019/9/15
-------------------------------------------------
   Change Activity:
                   2019/9/15:
-------------------------------------------------
"""
from rest_framework import serializers
from ..models import Permission

class PermissionListSerializer(serializers.ModelSerializer):
    '''
    权限列表序列化
    '''
    menuname = serializers.ReadOnlyField(source='menus.name')

    class Meta:
        model = Permission
        fields = ('id','name','method','menuname','pid')
