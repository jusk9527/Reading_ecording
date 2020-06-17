# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""

# 反向迭代

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 4
# 3
# 2
# 1

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(10)):
    print(rr)
for rr in Countdown(10):
    print(rr)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1