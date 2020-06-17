# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02 解压可迭代对象赋值给多个变量
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""


# -- 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？



## -- Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值，
    #  但如果有 24 个呢？这时候星号表达式就派上用场了：



# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)



record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = record

print(name)
# Dave
print(email)
# dave@example.com
print(phone_numbers)
# ['773-555-1212', '847-555-1212']



*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

print(trailing)
# [10, 8, 7, 1, 9, 5, 10]
print(current)
# 3




# 下面是一个带有标签的元组序列

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# foo 1 2
# bar hello
# foo 3 4


# 字符串的分割。

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

print(uname)
# nobody

print(homedir)
# /var/empty

print(sh)
# /usr/bin/false



# 你想解压一些元素后丢弃它们，你不能简单就使用 * ，
# 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(name)
# ACME

print(year)
# 2012

