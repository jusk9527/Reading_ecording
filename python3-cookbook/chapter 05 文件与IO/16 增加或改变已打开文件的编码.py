# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     16
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

# 增加或改变已打开文件的编码

## 你想在不关闭一个已打开的文件前提下增加或改变它的Unicode编码。

import urllib.request
import io

u = urllib.request.urlopen("https://www.baidu.com/")
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)


# <html>
# <head>
# 	<script>
# 		location.replace(location.href.replace("https://","http://"));
# 	</script>
# </head>
# <body>
# 	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
# </body>
# </html>

# 没带头就这样