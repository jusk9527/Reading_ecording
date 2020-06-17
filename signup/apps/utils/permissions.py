from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsOwnerOrReadOnly(BasePermission):
    """

    自己看自己的内容
    """
    message = "你没有权限查看"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #obj相当于数据库中的model，这里要把owner改为我们数据库中的user
        return obj.user == request.user




