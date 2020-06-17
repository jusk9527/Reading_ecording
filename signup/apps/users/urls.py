from django.urls import path,include
from users.views import ser_user,menu,oranization,role,permission
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', ser_user.UserViewSet, base_name="users")
router.register(r'organizations', oranization.OrganizationViewSet, base_name="organization")
router.register(r'menus', menu.MenuViewSet, base_name="menus")
router.register(r'permissions', permission.PermissionViewSet, base_name="permissions")
router.register(r'roles', role.RoleViewSet, base_name="roles")


urlpatterns = [

    path(r'api/', include(router.urls)),
    path(r'api/menu/tree/', menu.MenuTreeView.as_view(), name='menus_tree'),
    path(r'api/permission/tree/', permission.PermissionTreeView.as_view(), name='permissions_tree'),
    path(r'api/user/list/', ser_user.UserListView.as_view(), name='user_list'),
    path(r'api/organization/tree/', oranization.OrganizationTreeView.as_view(), name='organizations_tree'),
    path(r'api/organization/user/tree/', oranization.OrganizationUserTreeView.as_view(),name='organization_user_tree'),


    path(r'auth/login/', ser_user.UserAuthView.as_view()),
    path(r'auth/info/', ser_user.UserInfoView.as_view(), name='user_info'),
    path(r'auth/build/menus/', ser_user.UserBuildMenuView.as_view(), name='build_menus'),
]
