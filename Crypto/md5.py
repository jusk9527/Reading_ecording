import hashlib


if __name__ =="__main__":
    # 待加密信息
    str = "这是一个测试"
    # 创建MD5对象
    h = hashlib.md5()


    h.update(str.encode('utf-8'))
    print("MD5加密前:"+str)
    print("MD5加密后:"+h.hexdigest())


# MD5加密前:这是一个测试
# MD5加密后:cfca700b9e09cf664f3ae80733274d9f