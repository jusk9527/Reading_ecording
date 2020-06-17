# -- 你正在处理Unicode字符串，需要确保所有字符串在底层有相同的表示。

## -- 在Unicode中，某些字符能够用多个合法的编码表示。为了说明，考虑下面的这个例子：

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
# Spicy Jalapeño

print(s2)

# Spicy Jalapeño

print(s1 == s2)
# False


print(len(s1))
# 14

print(len(s2))
# 15


## -- 在需要比较字符串的程序中使用字符的多种表示会产生问题。 为了修正这个问题，
## -- 你可以使用unicodedata模块先将文本标准化
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
# True
print(ascii(t1))
# 'Spicy Jalape\xf1o'
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print(t3 == t4)
# True

print(ascii(t3))
# 'Spicy Jalapen\u0303o'