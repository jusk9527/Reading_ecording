# url编码

from urllib import parse

if __name__ =="__main__":
    data = parse.quote("岁月静好")
    turn_data = parse.unquote(data)

    print(data)
    print(turn_data)

# %E5%B2%81%E6%9C%88%E9%9D%99%E5%A5%BD
# 岁月静好