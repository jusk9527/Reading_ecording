import copy


class Cipher():
    def __init__(self, encodePassword, decodePassword):
        # 编码用的密码
        self.encodePassword = encodePassword
        # 解码用的密码
        self.decodePassword = decodePassword

    # 解码加密后的数据到原数据
    def encode(self, bs):
        for i,v in enumerate(bs):
            bs[i] = self.encodePassword[v]



    # 解密加密后的数据到原数据
    def decode(self, bs):
        for i,v in enumerate(bs):
            bs[i] = self.decodePassword[v]


    # 新建一个解密编辑器
    @classmethod
    def NewCipher(cls,encodePassword):
        decodePassword = copy.copy(encodePassword)

        for i,v in enumerate(encodePassword):
            decodePassword[v] = i

        return cls(encodePassword, decodePassword)




