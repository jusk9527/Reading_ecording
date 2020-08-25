"""TestCase_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from apps.Test import views
from apps.TestSyncio.views import TestAsyncioView
from apps.Test_djagno_apscheduler.views import test_add_task
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('hello_test_case', views.HelloTestCase.as_view(), name='hello_test_case'),
    # path('hello_test_case2', views.HomeWorkViewSet.as_view({'get': 'list'}), name='home_works_list'),

    # 异步写法
    path('testasyncioview/', TestAsyncioView.as_view(), name="testasyncioview"),

    # 任务、定时、配置
    path('testapscheduler/',test_add_task, name="testapscheduler")

]


import apps.Test_djagno_apscheduler.views