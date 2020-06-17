# 参考资料
# https://www.cxyxiaowu.com/1135.html
# https://blog.csdn.net/DCclient/article/details/102961599


# 求和
## 普通算法
def sum01():
    sum = 0
    for i in range(1,101):
        sum = sum+i
    return sum

sum01 = sum01()
print(sum01)




## 递归算法
### 思路 S100 = S99+100

def sum02(n):
    if n==1:
        return 1
    else:
        return sum02(n-1)+n

sum02 = sum02(100)
print(sum02)


## 斐波那契数列
### 题目：1、1、2、3、5、8、13、21、34、……,求解第n个数的值
### F(1)=1，F(2)=1,，F(n) = F(n-1) + F(n-2)（n>=3，n∈N*）。


def sum03(n):
    if n<=2:
        return 1
    else:
        return sum03(n-1) + sum03(n-2)

sum03 = sum03(30)
print(sum03)

## 阶乘问题
### n! = n * (n-1) * (n-2) * …* 1 (n>0)，求解第n个数的值
### n! = (n-1)! * n。令F(n) = n!，则F(n) = F(n-1) * n,由0! = 1，可以得出F(0) = 1

def sum04(n):
    if n==0:
        return 1
    else:
        return sum04(n-1)*n

sum04 = sum04(2)
print(sum04)


## 上楼梯问题
### 楼梯有n阶台阶，上楼可以一步上1阶，也可以一步上2阶，编一程序计算共有多少种不同的走法？
### F(x) = F(x-1)+F(x-2)

def sum05(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return sum05(n-1) +sum05(n-2)

sum05 = sum05(10)
print(sum05)

## 变态台阶问题
### 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
### 思路 F(X) = 2*F(X-1)

def sum06(n):
    if n==1:
        return 1
    else:
        return sum06(n-1) * 2

sum06 = sum06(3)
print(sum06)

## 泰波那契序列 Tn 定义如下： 

### T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
def sum07(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sum07(n - 1) + sum07(n - 2) + sum07(n - 3)

sum07 = sum07(4)
print(sum07)


## 结语
# 单次递归比较好理解，解题步骤：
# 1. 先弄清楚终止条件
# 2. 用数学方程式理解F（x）= .....
# 使用递归求解问题就好比，你手中有一把钥匙想要打开一扇门。当你打开面前这扇门，看到屋里面还有一扇门。
# 你走过去，发现手中的钥匙还可以打开它，你推开门，发现里面还有一扇门，你继续打开它。若干次之后，你打开面前的门后，
# 发现只有一间屋子，没有门了。然后，你开始原路返回，每走回一间屋子，你数一次，走到入口的时候，你可以回答出你到底用这你把钥匙打开了几扇门。
# 递归算法的应用十分广泛，应用递归算法可以使你的代码根据“优雅


## 优化建议
### 可以使用内存缓存cache有什么特点
### 尾递归：https://www.zhihu.com/question/20761771
### https://www.zhihu.com/people/lijigang.com/answers?page=2
### https://www.jianshu.com/p/4db970d8ddc1

res = []
res.append()

