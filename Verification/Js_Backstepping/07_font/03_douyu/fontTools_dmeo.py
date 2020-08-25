from fontTools.ttLib import TTFont
# TTFont()  用来打开woff文件的
movie_font = TTFont('mpepc5unpb.woff')
# 这里我们先看一下movie.off里面是什么样的
# 使用save()将拿到的文件数据保存为XML格式的文件
# movie_font.saveXML('mpepc5unpb.xml')
font_map= movie_font.getBestCmap()
print(font_map)

newmap= {}
for index, key in enumerate(font_map):
    value = font_map[key]
    # hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
    key = hex(key)
    newmap[key] = value
print(newmap)