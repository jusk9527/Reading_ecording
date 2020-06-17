# d导入DES模块
from Crypto.Cipher import DES
import binascii

# 这是秘钥

# key = b'abcdefgh'
# # 需要去生成一个DES对象
# des = DES.new(key, DES.MODE_ECB)
# # 需要加密的数据
# text = 'python spider'
# text = text + (8 - (len(text) % 8)) * '='
#
# # 加密的过程
# encrypto_text = des.encrypt(text.encode())
# encrypto_text = binascii.b2a_hex(encrypto_text)
# print(encrypto_text)
# b'084725d8f5ffafc68b7ddb6887c46c02'


from pyDes import des, ECB, PAD_PKCS5
import _base64

class Des():
    """
    des(key,[mode], [IV], [pad], [pad mode])
    key:必须正好8字节
    mode（模式）：ECB、CBC
    iv:CBC模式中必须提供长8字节
    pad:填充字符
    padmode:加密填充模式PAD_NORMAL or PAD_PKCS5

    注意：key这里为了简便就正好8字节，其实你可以自己定义key
    iv 确实必须提供8字节,不然错误
    """
    def __init__(self):
        pass
    def des_encrypt(self,s):
        secret_key = '1234A#CD'
        iv = secret_key
        k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(s.encode('utf-8'), padmode=PAD_PKCS5)
        return str(_base64.b64encode(en), 'utf-8')

    def des_descrypt(self,s):
        secret_key = '1234A#CD'
        iv = secret_key
        k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(_base64.b64decode(s), padmode=PAD_PKCS5)
        return de

if __name__ =="__main__":
    ds = Des()
    encrypt = ds.des_encrypt("hangzhou")

    decrypt = ds.des_descrypt(encrypt)

    print("加密:"+str(encrypt))
    print("解密:"+str(decrypt))


# 加密:7ZJq9IhUJVgiUJnvRAwmkA==
# 解密:b'hangzhou'
