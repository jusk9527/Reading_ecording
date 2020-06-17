from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets

from common.serializers import ProListSerializer
from common.models import ProList,LoginLogs,OperationLogs
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_extensions.cache.mixins import CacheResponseMixin




class ProListPagination(PageNumberPagination):
    '''
    问题列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class ProListViewSet(CacheResponseMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
        问题列表，分页
    '''


    #这里必须要定义一个默认的排序,否则会报错
    queryset = ProList.objects.all().order_by('id')
    pagination_class = ProListPagination
    serializer_class = ProListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)




