import copy
from rest_framework.viewsets import ModelViewSet
from ..models import Organization
from ..serializers.organization_serializer import OrganizationSerializer, \
    OrganizationUserTreeSerializer
from common.custom import CommonPagination, RbacPermission, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from common.custom import TreeSerializer,DepartmentSerializer
from rest_framework.views import APIView
from signup.basic import XopsResponse



class OrganizationViewSet(ModelViewSet, TreeAPIView):
    '''
    组织机构：增删改查
    '''
    perms_map = ({'*': 'admin'}, {'*': 'organization_all'}, {'get': 'organization_list'}, {'post': 'organization_create'},
    {'put': 'organization_edit'},{'delete': 'organization_delete'})
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name')
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (RbacPermission,)







class OrganizationTreeView(TreeAPIView):
    '''
    组织架构树
    '''
    queryset = Organization.objects.all()



class OrganizationUserTreeView(APIView):
    '''
    组织架构关联用户树
    '''
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        organizations = Organization.objects.all()
        serializer = OrganizationUserTreeSerializer(organizations, many=True)
        org_list = self.get_department_from_organization(request)

        tree_dict = {}
        tree_data = []
        for item in serializer.data:
            new_item = {
                'id':str(item['id']),
                'name': item['name'],
                'pid': item['pid'],
                'children': item['children']
            }
            tree_dict[item['id']] = new_item
        for i in tree_dict:
            if tree_dict[i]['pid']:
                pid = tree_dict[i]['pid']
                parent = tree_dict[pid]
                parent['children'].append(tree_dict[i])
            else:
                tree_data.append(tree_dict[i])

        return XopsResponse(tree_data)



class OrganizationUserTreeView(APIView):
    def getChildren(self, id, data):
        sz = []
        for obj in data:
            if obj["pid"] == id:
                sz.append({"id": obj["id"],"sort":obj["sort"], "name": obj["name"],
                           "children": self.getChildren(obj["id"], data)})
        return sz

    def get_org(self,school_name):
        organizations = Organization.objects.all()
        serializer = TreeSerializer(organizations, many=True)
        org = Organization.objects.filter(id=school_name).first()
        pid = org.id
        tree_data = []
        for item in serializer.data:
            new_item = {
                'id': item['id'],
                'name': item['name'],
                'pid': item['pid'],
                'sort': item['sort'],
            }
            tree_data.append(new_item)
        grade = self.getChildren(id=pid, data=tree_data)

        return grade

    def get_org_from_user(self, request):
        org_dict = {}
        org_data = []
        if request.user:
            org = request.user.department.values(
                "id",
                "name",
                # "pid",
                # "sort",
            ).distinct()
            serializer = DepartmentSerializer(org, many=True)

            for item in serializer.data:
                name = item["name"]
                id = item["id"]
                print(name)
                school = self.get_org(item["id"])
                org_dict["id"] = id
                org_dict["name"] = name

                org_dict["children"] = school
                m = copy.deepcopy(org_dict)
                org_data.append(m)

            return org_data
        else:
            pass


    def get_all_org_dic(self):
        """
        获取所有的组织架构,重组结构
        :return:
        """
        org = Organization.objects.all()
        serializer = TreeSerializer(org, many=True)
        tree_dict = {}
        tree_data = []
        for item in serializer.data:
            tree_dict[item['id']] = item
        for i in tree_dict:
            if tree_dict[i]['pid']:
                pid = tree_dict[i]['pid']
                parent = tree_dict[pid]
                parent.setdefault('children', []).append(tree_dict[i])
            else:
                tree_data.append(tree_dict[i])

        return tree_data

    def get_all_org(self, request):
        if request.user.is_superuser:
            tree_dict = self.get_all_org_dic()
        else:
            tree_dict = self.get_org_from_user(request)
        return tree_dict




    def get(self, request):
        """
        get:
            获取所有组织结构数据，重组结构
        """
        if request.user.id is not None:
            org_data = self.get_all_org(request)
            return XopsResponse(org_data)
        else:
            return XopsResponse('请登录后访问!')

