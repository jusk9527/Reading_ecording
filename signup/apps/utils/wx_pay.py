import time
import random
import hashlib
import requests


from bs4 import BeautifulSoup
from xml.etree import ElementTree as et
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from signup.settings import APPID, MCHID, KEY, NOTIFY_URL,SECRET                # 也可以放数据库里面




# 微信统一支付接口
class WeChatPay():
    def __init__(self, order_id, body, total_fee, nonce_str, openid, spbill_create_ip='115.200.192.213]'):
        """
        :param order_id: 订单编号 32字符内
        :param body: 订单信息
        :param total_fee: 订单金额 #单位为分
        :param nonce_str: 32位内随机字符串
        :param spbill_create_ip: 客户端请求IP地址
        :param openid: 客户openid
        appid = '微信appid'
        AppSecret = '微信AppSecret'
        mch_id = '微信商户id'
        api_key = '微信支付密钥'
        spbill_create_ip = '8.8.8.8' # 用户请求地址 终端IP 调用微信支付API的机器IP
        """
        self.api_key = 'xxxxxx'               # 商户秘钥
        self.params = {
            'appid': 'xxxxxxxxx',                              # appid
            'mch_id': 'xxxxxxxx',                                     # 商户号
            'nonce_str': nonce_str,
            'openid': openid,
            'body': str(body),
            'out_trade_no': str(order_id),
            'total_fee': str(int(total_fee)),
            'spbill_create_ip': spbill_create_ip,
            'trade_type': 'JSAPI',
            'notify_url': '',#你的支付回调地址
        }

        self.WxPay_request_url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'  # 微信请求url
        self.error = None




    def key_value_url(self, value):
        """
        将将键值对转为 key1=value1&key2=value2
        """
        string_sign = ''
        for k in sorted(value.keys()):
            string_sign += "{0}={1}&".format(k, value[k])
        return string_sign

    def get_sign(self, params):
        """
        生成sign 签名
        """
        stringA = self.key_value_url(params)
        stringSignTemp = stringA + 'key=' + self.api_key  # APIKEY, API密钥，需要在商户后台设置
        sign = hashlib.md5(stringSignTemp.encode('utf-8')).hexdigest().upper()
        params['sign'] = sign

        return sign

    def get_req_xml(self):
        """拼接XML
        """
        self.get_sign(self.params)
        xml = "<xml>"
        for k in sorted(self.params.keys()):
            xml += '<{0}>{1}</{0}>'.format(k, self.params[k])
        xml += "</xml>"
        return xml.encode('utf-8')

    def get_prepay_id(self):
        """
        请求获取prepay_id
        """

        xml = self.get_req_xml()
        unifiedorderXML = requests.post(self.WxPay_request_url, data=xml)
        unifiedorderXML.encoding ='utf-8'
        unifiedorderXML = unifiedorderXML.text
        root = et.fromstring(unifiedorderXML)
        if root.find("result_code").text != 'SUCCESS':
            self.error = u"连接微信出错啦！"
        prepay_id = root.find("prepay_id").text
        self.params['prepay_id'] = prepay_id
        # self.params['package'] = 'Sign=WXPay' # APP支付场景
        self.params['package'] = 'prepay_id=%s'%prepay_id   # JSAPI支付场景
        self.params['timestamp'] = str(int(time.time()))
        self.params['signType'] = 'MD5'

    def re_finall(self):
        """
        得到prepay_id后再次签名，返回给终端参数
        """
        self.get_prepay_id()
        if self.error:
            print('有错误发生')
            return

        sign_again_params = {
            'appId': self.params['appid'],
            'timeStamp': self.params['timestamp'],
            'nonceStr': self.params['nonce_str'],
            'package': self.params['package'],
            'signType': self.params['signType']
        }
        self.get_sign(sign_again_params)
        self.params['sign'] = sign_again_params['sign']

        # 移除其他不需要返回参数
        parms_keys = []
        for i in self.params.keys():
            parms_keys.append(i)
        for i in parms_keys:
            if i not in ['appid', 'mch_id', 'nonce_str', 'timestamp', 'sign', 'package', 'signType']:
                self.params.pop(i)
        return self.params



class Wxpay(APIView):
    """
    统一下单
    """
    def get_user_info(self, js_code):

        """
        使用 临时登录凭证code 获取 session_key 和 openid 等
        支付部分仅需 openid，如需其他用户信息请按微信官方开发文档自行解密
        """
        req_params = {
            'appid': APPID,
            'secret': SECRET,
            'js_code': js_code,
            'grant_type': 'authorization_code',
        }
        user_info = requests.get('https://api.weixin.qq.com/sns/jscode2session',
                                 params=req_params, timeout=3, verify=False)
        return user_info.json()


    def get_nonce_str(self):
        base_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        random_str = ''.join(random.sample(base_str, 32))
        return random_str


    def get(self,request):
        """
        统一下单
        :param request:
        :return:
        """
        code = request.GET.get("code", None)
        openid = self.get_user_info(code)['openid']
        WxPay = WeChatPay(order_id=self.get_nonce_str(), body="小张南山店-超市", total_fee=int(1), nonce_str=self.get_nonce_str(),
                       openid=openid, spbill_create_ip='118.24.132.204')
        finall = WxPay.re_finall()
        return Response(finall)




class wxpayNotify(APIView):
    """
    支付回调
    """

    def trans_xml_to_dict(self, data_xml):
        soup = BeautifulSoup(data_xml, features='xml')
        xml = soup.find('xml')  # 解析XML
        if not xml:
            return {}
        data_dict = dict([(item.name, item.text) for item in xml.find_all()])
        return data_dict

    def key_value_url(self,value):
        """
        将将键值对转为 key1=value1&key2=value2
        """
        string_sign = ''
        for k in sorted(value.keys()):
            string_sign += "{0}={1}&".format(k, value[k])
        return string_sign


    def get_sign(self,params):
        """
        生成sign 签名
        """
        api_key = 'xxxxx'
        stringA = self.key_value_url(params)
        stringSignTemp = stringA + 'key=' + api_key  # APIKEY, API密钥，需要在商户后台设置
        sign = hashlib.md5(stringSignTemp.encode('utf-8')).hexdigest().upper()
        params['sign'] = sign

        return sign

    def post(self, request):
        _xml = request.data
        xml = str(_xml, encoding="utf-8")
        tree = et.fromstring(xml)


        return_code = tree.find("return_code").text         # xml 解析
        data_dict = self.trans_xml_to_dict(_xml)
        sign = data_dict.pop('sign')                        # 取出签名
        back_sign = self.get_sign(data_dict)                # 计算签名
        if (sign == back_sign):
            try:
                if return_code == 'FAIL':
                    # 官方发出错误
                    return HttpResponse("""<xml><return_code><![CDATA[FAIL]]></return_code>
                                                <return_msg><![CDATA[Signature_Error]]></return_msg></xml>""",
                                        content_type='text/xml', status=200)
                elif return_code == 'SUCCESS':
                    # 拿到自己这次支付的 out_trade_no
                    _out_trade_no = tree.find("out_trade_no").text

                    total_fee = tree.find("total_fee").text

                    return HttpResponse("""<xml><return_code><![CDATA[SUCCESS]]></return_code>
                                            <return_msg><![CDATA[OK]]></return_msg></xml>""",
                                        content_type='text/xml', status=200)

                    # 这里省略了 拿到订单号后的操作 看自己的业务需求

            except Exception as e:
                print("支付出错")
                return HttpResponse("""<xml><return_code><![CDATA[FAIL]]></return_code>
                                                            <return_msg><![CDATA[Signature_Error]]></return_msg></xml>""",
                                    content_type='text/xml', status=200)
        else:
            print("签名错误")
            return HttpResponse("""<xml><return_code><![CDATA[FAIL]]></return_code>
                                                                    <return_msg><![CDATA[Signature_Error]]></return_msg></xml>""",
                                content_type='text/xml', status=200)
        pass









