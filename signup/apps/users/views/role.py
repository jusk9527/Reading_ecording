from ..models import Role
from rest_framework.viewsets import ModelViewSet
from ..serializers.role_serializer import RoleListSerializer, RoleModifySerializer
from common.custom import CommonPagination, RbacPermission
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication



class RoleViewSet(ModelViewSet):
    '''
    角色管理：增删改查(全局)

    list:
        获取所有角色+id获取某人具体信息
    create:
        添加一个角色
    delete:
        删除一个角色
    update:
        修改一个角色
    '''
    perms_map = ({'*': 'admin'}, {'*': 'role_all'}, {'get': 'role_list'}, {'post': 'role_create'}, {'put': 'role_edit'},
                 {'delete': 'role_delete'})
    queryset = Role.objects.all()
    serializer_class = RoleListSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (RbacPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return RoleListSerializer
        return RoleModifySerializer
