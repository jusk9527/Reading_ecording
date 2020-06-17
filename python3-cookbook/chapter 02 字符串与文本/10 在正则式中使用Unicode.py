# -- 你正在使用正则表达式处理文本，但是关注的是Unicode字符处理。

## -- 默认情况下 re 模块已经对一些Unicode字符类有了基本的支持。
## -- 比如， \\d 已经匹配任意的unicode数字字符了：

import re
num = re.compile('\d+')

res_first = num.match('123')
print(res_first)
# <_sre.SRE_Match object; span=(0, 3), match='123'>


## -- 如果你想在模式中包含指定的Unicode字符，你可以使用Unicode字符对应的转义序列(比如 \uFFF 或者 \UFFFFFFF )。
## -- 比如，下面是一个匹配几个不同阿拉伯编码页面中所有字符的正则表达式：


arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')


## -- 当执行匹配和搜索操作的时候，最好是先标准化并且清理所有文本为标准化格式(参考2.9小节)。
## -- 但是同样也应该注意一些特殊情况，比如在忽略大小写匹配和大小写转换时的行为。


pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
# <_sre.SRE_Match object; span=(0, 6), match='straße'>

pat.match(s.upper())
print(s.upper())
# STRASSE





