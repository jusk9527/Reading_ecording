from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

def signature(message, rsa_path):
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode())
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)

        return signature

def verify_signature(message, signature, pub_rsa_path):
    '''验证签名'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(message.encode())
        print(digest)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify


if __name__ == "__main__":
    plain = 'message'

    pub_rsa_path = "./public_key.txt"
    rsa_path = "./private_key.txt"

    sign = signature(plain, rsa_path)
    print('签名：', sign)
    flag = verify_signature(plain, sign, pub_rsa_path)
    print('验证结果：', flag)


# 签名： b'tF/zf1NeZpU54ws+gfW+gSb3IuBiuRf/7tfdebOKxo0S0W2BtdDvU56QTvkwPrVaqnHSgNgpbWjI8Gl+ZGaPYNe+skXEHm5se24Zfl2dosCVhp7d8ChFIxWd30oqg1qxjZU0M+tLuSyUyLZGhdRsb1s8C/O0K/suCN17TpEnA1pRv+/Q6+4pJ49IKWB7RoalauaAGXN0JU8wb8Lfv32k73nJ3l338JXSnMpy6xWt0P8E2nZlFU3VMPWIVzUfOUnyDYG2v/uA7coxxegpggm6PNpWnPkhlAKowbi/kHntq1V5wk5Gv8uB9vT0fqXGbCTcIY3kdiIk+/vz6EzpE5Xzhg=='
# <Crypto.Hash.SHA1.SHA1Hash object at 0x02528BF0>
# 验证结果： True