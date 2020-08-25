# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
#     'Cookie': 'isfirst=789kq7uc1pp4c',
#
# }
# res = requests.get(url="http://www.porters.vip/confusion/food.html",headers=headers)
# print(res.text)

# 定义映射关系
mappings = {'vhk08k': 0, 'vhk6zl': 1, 'vhk9or': 2,
'vhkfln': 3, 'vhkbvu': 4, 'vhk84t': 5,
'vhkvxd': 6, 'vhkqsc': 7, 'vhkjj4': 8,
'vhk0f1': 9}
# 商家联系电话class 属性
html_d_class = ['vhkbvu', 'vhk08k', 'vhk08k',
'', 'vhk84t', 'vhk6zl',
'vhkqsc', 'vhkqsc', 'vhk6zl']
phone = [mappings.get(i) for i in html_d_class]
# 将映射后的结果打印输出
print(phone)
