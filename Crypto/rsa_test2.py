from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


class RSAENDE():
    """
    公钥加密，私钥解密
    """
    def __init__(self):
        # 伪随机数生成器
        self.random_generator = Random.new().read
        # rsa算法生成实例
        self.rsa = RSA.generate(1024, self.random_generator)

    def encrypt(self,message, pub_rsa_path):
        '''使用公钥加密'''
        with open(pub_rsa_path) as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
            return cipher_text

    def decrypt(self,secret_message, rsa_path):
        '''使用私钥解密'''
        with open(rsa_path) as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            text = cipher.decrypt(base64.b64decode(secret_message), self.random_generator)
            return text


if __name__ == "__main__":
    plain = 'message'
    pub_rsa_path = "./public_key.txt"
    rsa_path = "./private_key.txt"

    rsaende = RSAENDE()
    print('明文：', plain)
    secret = rsaende.encrypt(plain, pub_rsa_path)

    print('加密文：', secret)
    text = rsaende.decrypt(secret, rsa_path)

    print('解密文：', text)


# 明文： message
# 加密文： b'iTvbkc5z4P1b8UsuoAox/xLxjBPu4S1cjdnR+uwGUbHE2LcfUj894kV5CUVyzd4EEfNr/GilTVnh56ocxiD5MHD44+R11rfea7Th7F1rhzf19VSi9/BlVew0Ba/JqSZUbGrvsPVSOkJEwsJSJAUYcKfehPrwo7IXYUjPxKXC48gzSdKCS8VTa4Jr3wWYHOg5y0PbvkOQZxYKzv/eF23UbLnht770bT3O7tvc9ImYMxNjgU3fgQ+m+e+D2yWwSx4mFXVPcpJcij1UqV8qjd8zqJwjaO4CZPngkGh2vETcNDjY8q9v0deiLIDrX3N5IGW2TKaYf+/worKdbT4XZDKrXA=='
# 解密文： b'message'