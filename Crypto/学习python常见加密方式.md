---
title: 学习python常见加密方式
date: 2019-04-21 11:43:39
tags: 加密 解密
categories: js解密

---

![](../学习python常见加密方式/08.png)

<!--more-->

### 前言

我们的加密实现方式是对二进制编码的格式进行加密的。也就是Bytes

字符串与Bytes互转，使用encode()和decode()方法


encode()| decode()
---|---
str----->bytes | bytes----->str
data = "岁月静好".encode()---->b'\xe5\xb2\x81\xe6\x9c\x88\xe9\x9d\x99\xe5\xa5\xbd'|turn_data = data.decode()---->岁月静好

两位十六进制常用来显示一个二进制字节

利用==binascii==模块可以将十六进制显示的字节转换成我们在加密中更常用的方式



```
import binascii
data = binascii.b2a_hex('岁月静好'.encode())
print(data)
```
结果
```
b'e5b281e69c88e99d99e5a5bd'
```


```
data = binascii.a2b_hex(b'e5b281e69c88e99d99e5a5bd')
print(data)
```

结果

```
b'\xe5\xb2\x81\xe6\x9c\x88\xe9\x9d\x99\xe5\xa5\xbd'
```


```
data = binascii.a2b_hex(b'e5b281e69c88e99d99e5a5bd').decode()
print(data)
```

结果

```
岁月静好
```

总结

binascii

方法 | 作用
---|---
b2a_hex() | 字符串转16进制
a2b_hex() | 16进制转 字符串

#### URL 编码

正常的url中只包含ASCII字符串，也就是字符、数字和一些符号。而URL编码就是一种浏览器用来避免url中出现特殊字符（如汉字）的编码方式

其实就是将超出ASCII范围的字符转换成带%的是十六进制格式

例如：

```
from urllib import parse
data = parse.quote('岁月静好')
print(data)
turn_data = parse.unquote(data)
print(turn_data)
```


```
%E5%B2%81%E6%9C%88%E9%9D%99%E5%A5%BD
岁月静好
```


#### Base64 编码

Base64是一种用64个字符来表示任意二进制数据的方法

Base64 编码可以成为密码学的基石，可以将任意的二进制数据进行Base64编码。 所有的数据都能被编码为并只用65个字符就能表示的文本文件


#### MD5 (信息-摘要算法)

message-digest algorithm 5（信息-摘要算法）。经常说的“MD5加密”，就是信息摘要算法。

md5, 其实就是一种算法，可以将一个字符串，或文件，或压缩包，执行md5后，就可以生成一个固定长度128bit的串，这个串，基本上是唯一的


> 特点

1. 压缩性，任意铲毒的数据，算出的MD5值长度都是固定的
2. 容易计算：从原数据计算出MD5值很容易
3. 抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别
4. 强抗碰撞：已知源数据和其MD5值，想到一个具有相同MD5值的数据（即诶找数据）是非常困难的
5. ==不可逆性==：每个人都有不同的指纹，看到这个人，可以得出他的指纹等信息，并且唯一对应，但你只看到或读取到这个人的长相或身份等信息
6. 



```
import hashlib

# 待加密信息
str = '这是一个测试'

# 创建md5对象
h = hashlib.md5()

# 此处鼻血声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing

h.update(str.encode(encoding='utf-8'))

print('MD5加密前为：' + str)
print('MD5加密后为:' + h.hexdigest())
```

结果

```
MD5加密前为：这是一个测试
MD5加密后为:cfca700b9e09cf664f3ae80733274d9f
```


md5的长度，默认为128bit, 也就是128个0和1的二进制。这样表达是很不友好的，所以将二进制转16进制，每4个bit表示一个16进制，所以128/4=32换成16进制表示后，为32位

为什么网上还有md5是16进制呢？

其实16位的长度，是从32为md5值来的，是将32位md5去掉前八位，去掉后八位得到的


#### 第三方包PyCryptodome
PyCrypto 是Python 中国密码学方面最有名的第三方软件包，提供了许多加密算法的使用，可惜的是，他的开发工作于2012年就停止


但是他的一个分支PyCrytodome 取代了PyCrypto

> linux

```
pip install pycryptodome
```
> 导入


```
import Crypto
```

> windows


```
pip install pycryptodomex
```

> 导入


```
import Cryptodome
```

#### DES

DES 算法为密码体质中的对称密码体质，又被称为美国数据加密标准

DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法

DES 算法的入口参数有三个：Key、Data、Mode。其中Key为7个字节共56位，是DES算法的工作秘钥;Data 为8个字节64位，是要被加密或解密的数据；Mode为DES的工作方式，有两种：加密或解密


秘钥长64位，秘钥事实上是56位参与DES运算（第8、16、24、32、40、48、56、64）是校验位，使得每个秘钥都有奇数个1),分组后的明文组和56位的秘钥按位替换或交换的方法形成的密文组

##### python 使用


```
# d导入DES模块
from Crypto.Cipher import DES
import binascii

# 这是秘钥

key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider'
text = text + (8 - (len(text) % 8)) * '='

# 加密的过程
encrypto_text = des.encrypt(text.encode())
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)
```

结果

```
b'084725d8f5ffafc68b7ddb6887c46c02'
```

#### 3DES
升级版DES

由于计算机运算能力的增强，原版DES密码的秘钥长度变得容易被暴力破解。
3DES即是设计用来提供一种相对简单的方法，即通过增加DES的秘钥长度来避免类似的攻击，而不是设计一种全新的块密码算法

3DES 是DES向AES过渡的加密算法（1999年，NIST将3-DES指定为过渡的加密标准）, 加密算法，其具体算法如下：

设 Ek()和Dk()代表DES算法的加密和解密过程，K代表DES算法使用的秘钥，M代表明文，C代表密文，这样;

3DES 加密过程为 ：C=EK3(DK2(EK1(M)))
3DES 解密过程为：M=Dk(EK2(Dk3(C)))

```
# d导入DES模块
from Crypto.Cipher import DES
import binascii

# 这是秘钥

key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider'
text = text + (8 - (len(text) % 8)) * '='

# 加密的过程
encrypto_text = des.encrypt(text.encode())
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)
```


```
b'084725d8f5ffafc68b7ddb6887c46c02'
```



#### AES
高级加密标准，在软件以及硬件上都能快速地解密，相对来说较易于实现，且还需要很少的存储器，作为一个新的加密标准，目前正被部署应用到更广大的范围。


##### 特点

1. 抵抗所有已知的攻击
2. 在多个平台上速度快，编码紧凑
3. 设计简单


![image](../学习python常见加密方式/clipboard.png)

AES为分组密码，分组密码也就是把明文分成一组一组的，没组长度相等，每次加密一组数据，直到加密完整个明文，在AES标准中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位），秘钥的长度可以使用128位、192位或256位。秘钥的长度不同，推荐加密轮速也不同。

一般常用语128位

python 实现


```
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex


# 要加密的明文
data = '南来北往'
# 秘钥Key 长度必须为16(AES-128)、24(AES-192)、或32(AES-256) Bytes 长度
# 目前AES-128足够用
key =b'this is a 16 key'
# 生成铲毒等于AES块大小的不可重复的秘钥向量
iv = Random.new().read(AES.block_size)

# 使用key和iv初始化AES对象，使用MOOE_CEB模式
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数

# 将iv(秘钥向量) 加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode())

# 解密的话要用key和iv生成新的AES对象
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
decrypttext = mydecrypt.decrypt(ciphertext[16:])


print('秘钥k为:', key)
print('iv为:', b2a_hex(ciphertext)[:16])
print('加密后数据为:', b2a_hex(ciphertext)[16:])
print('解密后数据为:', decrypttext.decode())
```

运行结果

```
秘钥k为: b'this is a 16 key'
iv为: b'638828724f733563'
加密后数据为: b'e4a39d98e94872cd918b6e694bca944f6c644982'
解密后数据为: 南来北往
```


#### RSA

RSA 加密算法是一种非对称加密算法。在公开秘钥加密和电子商业中RSA被广泛使用

改算法基于一个简单的数论事实：将两个大素数相乘十分容易，但那是想要对其乘积进行因式分解却及其困难，因此可以将乘积公开作为加密秘钥。即公钥，而两个大素数组合成私钥。公钥是可发布的供任何人使用，私钥则为自己所有，供解密之用

##### 非对称加密

典型的如RSA等，常见方法，使用openssl, keytools等工具生成一堆公钥对，使用被公钥加密的数据可以使用私钥来解密
，反之亦然（被私钥加密的数据也可以被公钥解密）。

在实际使用中是要一般保存在发布者手中，是私有的不对外公开的，只将公钥对外公布，就能实现只要私钥的持有者才能将数据解密的方法，这种加密方式安全性很高，因为他不用将解密的秘钥进行传递。从而灭有秘钥在传递过程中被截获的风险，而破解密文几乎又是不吭你的


但是算法的效率低，所以常用语很重要数据的加密，常和对称配合使用，使非对称加密的秘钥去加密对称加密的秘钥.

##### python 实现

首先安装一个rsa模块


```
import rsa
import binascii

# 使用网页中会的的n和e值，将明文加密
def rsa_encrypt(rsa_n, rsa_e, message):
    # 用n值和e值生成公钥
    key = rsa.PublicKey(rsa_n, rsa_e)
    # 用公钥把明文加密
    message = rsa.encrypt(message.encode(), key)
    # 转化成常用的可读性高的十六进制
    message = binascii.b2a_hex(message)
    # 将加密结果转化回字符串并返回
    return message.decode()

# RSA的公钥有两个值n和e,我们在网站中获得的公钥一般就是这样的两个值
# n常常为长度为526的十六进制字符串
# e常常为十六进制‘10001’
pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
pubkey_e = '10001'

# 需要将十六进制转换成十进制
rsa_n = int(pubkey_n, 16)
rsa_e = int(pubkey_e, 16)
# 要加密的明文
message = '南北今天很忙'

print('公钥n值长度：', len(pubkey_n))
print(rsa_encrypt(rsa_n, rsa_e, message))
```

结果

```
公钥n值长度： 256
41adc4d100f7df49bb2938edbcefe3bd2f1e63e6ccdf29fe7146ed9f837e510e4d8c249d2b60fa747bc0684c5f5901a4da6cab79dcd264724bf1c8bed13a281043be9705d598877c39b23379ea8115f350e8443901076f6ccdcdcdac98783a8fddcfdd6b67b4c97153af4bc908452eb4c98fb103dcc28417a0c6468e99b74c9d
```

参考资料：https://www.jianshu.com/p/4ba20afacce2

































