# 字符串转---》16进制

import binascii

if __name__ =="__main__":
    en_data = binascii.b2a_hex("岁月静好".encode())
    de_data = binascii.a2b_hex(b"e5b281e69c88e99d99e5a5bd").decode()
    print(en_data)

    print(de_data)


# b'e5b281e69c88e99d99e5a5bd'
# 岁月静好

