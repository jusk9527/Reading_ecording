from signup.basic import XopsResponse
from rest_framework import permissions
from rest_framework import serializers

from rest_framework.generics import ListAPIView
from rest_framework.views import exception_handler
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication






import logging


error_logger = logging.getLogger('error')
info_logger = logging.getLogger('info')


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #obj相当于数据库中的model，这里要把owner改为我们数据库中的user
        return obj.user == request.user

class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)



def xops_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        msg = '失败' if response.status_code >= 400 else '成功'
        notification_response = {}
        notification_response['code'] = response.status_code
        notification_response['message'] = msg
        notification_response['detail'] = response.data
        response.data = notification_response
    return response




class CommonPagination(PageNumberPagination):
    '''
    分页设置
    '''
    page_size = 10
    page_size_query_param = 'size'



class RbacPermission(BasePermission):
    '''
    自定义权限
    '''

    @classmethod
    def get_permission_from_role(self, request):
        try:
            perms = request.user.roles.values(
                'permissions__method',
            ).distinct()
            return [p['permissions__method'] for p in perms]
        except AttributeError:
            return None

    def has_permission(self, request, view):
        perms = self.get_permission_from_role(request)
        print(hasattr(view, 'perms_map'))
        if perms:
            if 'admin' in perms:
                return True

            # 没有permas_map就是超级管理员
            elif not hasattr(view, 'perms_map'):
                return True
            else:
                perms_map = view.perms_map
                _method = request._request.method.lower()
                for i in perms_map:
                    for method, alias in i.items():
                        if (_method == method or method == '*') and alias in perms:
                            return True




class ObjPermission(BasePermission):
    '''
    密码管理对象级权限控制
    '''

    def has_object_permission(self, request, view, obj):
        perms = RbacPermission.get_permission_from_role(request)
        if 'admin' in perms:
            return True
        elif request.user.id == obj.uid_id:
            return True




class TreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    pid = serializers.PrimaryKeyRelatedField(read_only=True)
    sort = serializers.CharField(max_length=20)






class TreeAPIView(ListAPIView):
    '''
    自定义树结构View
    '''
    serializer_class = TreeSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())


        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        tree_dict = {}
        tree_data = []
        try:
            for item in serializer.data:
                tree_dict[item['id']] = item
            for i in tree_dict:
                if tree_dict[i]['pid']:
                    pid = tree_dict[i]['pid']
                    parent = tree_dict[pid]
                    parent.setdefault('children', []).append(tree_dict[i])
                else:
                    tree_data.append(tree_dict[i])
            results = tree_data
            print(results)
        except KeyError:
            results = serializer.data
        if page is not None:
            return self.get_paginated_response(results)

        return XopsResponse(results)




