# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 用Shell通配符匹配字符串

from fnmatch import fnmatch, fnmatchcase

res = fnmatch('foo.txt', '*.txt')
print(res)
# True
res = fnmatch('foo.txt', '?oo.txt')
print(res)
# True
res = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(res)
# True


## mac
res = fnmatch('foo.txt', '*.TXT')
print(res)
# False

## window
res = fnmatch('foo.txt', '*.TXT')
print(res)
# True


# 完全使用你的模式大小写匹配
res = fnmatchcase('foo.txt', '*.TXT')
print(res)


from fnmatch import fnmatchcase
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
res = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(res)
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']