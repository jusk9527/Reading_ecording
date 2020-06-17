from django.urls import path,include,re_path
from django.views.static import serve
from signup.settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from signup import settings
router = DefaultRouter()



urlpatterns = [
    re_path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs/',include_docs_urls(title='xxxxxxx')),

    # 支付
    # path('{0}/wepay1'.format(client), WxpayView.as_view(), name="wepay1"),


    # 支付回调
    # path('{0}/wxpayNotify'.format(client),WxpayNotify.as_view(), name="wxpayNotify"),

    # user的接口
    path(r'', include('users.urls')),










]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

