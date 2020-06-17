from Crypto.Cipher import DES3
import _base64



class Des3:
    """
    new(key, mode, *args, **kwargs)
    key:必须8bytes倍数介于16-24
    mode：
    iv:初始化向量适用于MODE_CBC、MODE_CFB、MODE_OFB、MODE_OPENPGP，4种模式
        ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB``长度为8bytes
        ```MODE_OPENPGP```加密时8bytes解密时10bytes
        未提供默认随机生成
    nonce：仅在 ``MODE_EAX`` and ``MODE_CTR``模式中使用
            ``MODE_EAX``建议16bytes
            ``MODE_CTR``建议[0, 7]长度
            未提供则随机生成
    segment_size：分段大小，仅在 ``MODE_CFB``模式中使用，长度为8倍数，未指定则默认为8
    mac_len： 适用``MODE_EAX``模式，身份验证标记的长度（字节），它不能超过8（默认值）
    initial_value：适用```MODE_CTR```，计数器的初始值计数器块。默认为**0**。
    """
    def __init__(self, key):
        self.key = key
        self.mode = DES3.MODE_ECB

    def encrypt(self, text):
        """
        传入明文
        :param text:bytes类型，长度是KEY的倍数
        :return:
        """
        if not isinstance(text, bytes):
            text = bytes(text, 'utf-8')
        x = len(text) % 8
        text = text+b'\0'*x
        cryptor = DES3.new(self.key, self.mode)
        ciphertext = cryptor.encrypt(text)
        return ciphertext

    def decrypt(self, text):
        cryptor = DES3.new(self.key, self.mode)
        plain_text = cryptor.decrypt(text)
        st = str(plain_text.decode("utf-8")).rstrip('\0')
        return st

# https://www.cnblogs.com/crazyrunning/p/7382693.html
if __name__ =="__main__":
    des3_test = Des3(b"123456789qazxswe")
    a = des3_test.encrypt("测试加密".encode())
    print('加密:' + str(_base64.b64encode(a)))
    de_data = des3_test.decrypt(a)
    print('解密:'+str(de_data))


# 加密:b'0GKV0qw2Y3lm9wouhxbvcw=='
# 解密:测试加密