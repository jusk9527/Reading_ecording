# -- 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配

## -- 这个问题很典型的出现在当你用点(.)去匹配任意字符的时候，忘记了点(.)不能匹配换行符的事实。
## -- 比如，假设你想试着去匹配C语言分割的注释：

import re
comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a
            multiline comment */
        '''

res_first = comment.findall(text1)
print(res_first)
# [' this is a comment ']



res_two = comment.findall(text2)
print(res_two)
# []



## -- re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。
## -- 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
res_three = comment.findall(text2)
print(res_three)
# [' this is a\n            multiline comment ']


