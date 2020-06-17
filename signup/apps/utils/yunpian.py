import requests
import json

class YunPian(object):
    """
    https://www.yunpian.com/

    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "xxxxx".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == "__main__":
    yun_pian = YunPian("xxxx")
    yun_pian.send_sms("2018", "手机号码")



