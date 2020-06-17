# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     menu
   Description :
   Author :       jusk?
   date：          2019/9/15
-------------------------------------------------
   Change Activity:
                   2019/9/15:
-------------------------------------------------
"""
from rest_framework.viewsets import ModelViewSet
from ..models import Menu
from ..serializers.menu_serializer import MenuSerializer
from common.custom import CommonPagination,RbacPermission,TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import SessionAuthentication


class MenuViewSet(ModelViewSet, TreeAPIView):
    '''
    菜单管理：增删改查(全局)

    权限树

    list:
        获取菜单+id具体菜单
    create:
        添加一个菜单
    delete:
        删除一个菜单
    update:
        修改一个菜单
    '''

    perms_map = ({'*': 'admin'}, {'*': 'menu_all'}, {'get': 'menu_list'}, {'post': 'menu_create'}, {'put': 'menu_edit'},
                 {'delete': 'menu_delete'})
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('name',)
    ordering_fields = ('sort',)
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    authentication_classes = (SessionAuthentication,)
    permission_classes = (RbacPermission,)



class MenuTreeView(TreeAPIView):
    '''
    菜单树

    list:
        获取菜单树
    '''
    queryset = Menu.objects.all()