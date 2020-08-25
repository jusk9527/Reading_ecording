# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response



from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.Test.models import HomeWork
from apps.Test.serializers import HomeWorkSerializer


class HomeWorkViewSet(ReadOnlyModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer
    permission_classes = (IsAuthenticated, )


class HelloTestCase(APIView):
    def get(self, request, *args, **kwargs):

        data = {
            'msg': 'Hello %s I am a test Case' % request.query_params.get('name', ',')
        }

        # 请求头,这里的http请求头写法要加HTTP_
        test_header = request.META.get('HTTP_TEST_HEADER')
        if test_header:
            data['test_header'] = test_header


        return Response(data)
        # return Response({
        #     'msg': 'Hello %s I am a test Case' % request.query_params.get('name', ',')
        # })
