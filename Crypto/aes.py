from Crypto.Cipher import AES
import _base64

class Aes():
    """
    AES
    除了MODE_SIV模式key长度为：32, 48, or 64,
    其余key长度为16, 24 or 32
    详细见AES内部文档
    CBC模式传入iv参数
    本例使用常用的ECB模式
    """

    def __init__(self, key):
        if len(key) > 32:
            key = key[:32]
        self.key = self.to_16(key)

    def to_16(self, key):
        """
        转为16倍数的bytes数据
        :param key:
        :return:
        """
        key = bytes(key, encoding="utf8")
        while len(key) % 16 != 0:
            key += b'\0'
        return key  # 返回bytes

    def aes(self):
        return AES.new(self.key, AES.MODE_ECB) # 初始化加密器

    def encrypt(self, text):
        aes = self.aes()
        return str(_base64.encodebytes(aes.encrypt(self.to_16(text))),
                   encoding='utf8').replace('\n', '')  # 加密

    def decodebytes(self, text):
        aes = self.aes()
        return str(aes.decrypt(_base64.decodebytes(bytes(
            text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))  # 解密

if __name__ =="__main__":
    aes = Aes("assssssssdfasasasasa")
    en_data = aes.encrypt("hangzhou")
    de_data = aes.decodebytes(en_data)
    print("加密:"+str(en_data))
    print("解密:"+str(de_data))


# 加密:b+pGiZF0y7UqrlV97aGx9w==
# 解密:hangzhou