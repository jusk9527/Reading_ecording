# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cli_user
   Description :
   Author :       jusk?
   date：          2019/9/15
-------------------------------------------------
   Change Activity:
                   2019/9/15:
-------------------------------------------------
"""

from rest_framework.views import APIView
import requests
from signup.settings import APPID, SECRET
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()

class ClientUserLogin(APIView):
    """
    客户端用户登录
    """

    def __init__(self):
        """
        WX_APP_APPID: appid
        WX_APP_SECRET: appsecret
        """
        self.WX_APP_APPID = APPID
        self.WX_APP_SECRET = SECRET

    def get_user_info_func(self, user_code):
        api_url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'
        get_url = api_url.format(APPID,SECRET,user_code)
        r = requests.get(get_url)
        return r.json()

    def login_or_create_account(self, json_data):
        openid = json_data['openid']
        session_key = json_data['session_key']
        try:
            user = User.objects.get(username=openid)
        except:
            user = None
        if user:
            pass
        else:
            # 注册新用户
            user = User.objects.create(
                username=openid,
                password=openid,
                session_key=session_key,
            )
        user.save()

        try:
            from rest_framework_jwt.settings import api_settings

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            res = {
                'status': 200,
                'message':"验证成功",
                'token': token
            }
        except Exception as e:
            res = {
                'status': 500,
                'message': '你好！jwt验证失败'
            }
        return res



    def post(self, request):

        """
        post:
        小程序登录
        参数列表：
            user_code：微信code

            返回参数：
            status: 200,
            message: 验证成功,
            token: token

        """
        user_code = request.data["user_code"]
        json_data = self.get_user_info_func(user_code)
        res = self.login_or_create_account(json_data)
        return Response(res)

