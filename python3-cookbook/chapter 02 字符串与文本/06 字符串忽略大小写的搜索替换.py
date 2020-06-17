# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     06
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""
# 字符串忽略大小写的搜索替换
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
res = re.findall('python', text, flags=re.IGNORECASE)
print(res)

# ['PYTHON', 'python', 'Python']

res = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(res)

# UPPER snake, lower snake, Mixed snake

## 缺点是不能大小写一致

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


res = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(res)

# UPPER SNAKE, lower snake, Mixed Snake

