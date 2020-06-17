
from ..models import Permission

from rest_framework.viewsets import ModelViewSet
from ..serializers.permission_serializer import PermissionListSerializer
from common.custom import CommonPagination, RbacPermission, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication




class PermissionViewSet(ModelViewSet, TreeAPIView):
    '''
    权限：增删改查

    list:
        获取一份权限+id具体权限详情
    create:
        添加一个权限
    delete:
        删除一个权限
    update:
        修改一个权限
    '''
    perms_map = ({'*': 'admin'}, {'*': 'permission_all'}, {'get': 'permission_list'}, {'post': 'permission_create'},
                 {'put': 'permission_edit'},{'delete': 'permission_delete'})
    queryset = Permission.objects.all()
    serializer_class = PermissionListSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # permission_classes = (RbacPermission,)


class PermissionTreeView(TreeAPIView):
    '''
    权限树

    list:
        获取所有权限
    '''
    queryset = Permission.objects.all()
