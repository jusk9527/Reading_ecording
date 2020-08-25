from fontTools.ttLib import TTFont
# TTFont()  用来打开woff文件的
movie_font = TTFont('01_movie.woff')
# 这里我们先看一下movie.off里面是什么样的
# 使用save()将拿到的文件数据保存为XML格式的文件
movie_font.saveXML('01_movie.xml')
font_map= movie_font.getBestCmap()
print(font_map)

newmap= {}
# for index, key in enumerate(font_map):
#     value = font_map[key]
#     # hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
#     key = hex(key)
#     newmap[key] = value
# print(newmap)



relation_table = {'uniE9C7': '7', 'uniF57B': '1', 'uniE7DF': '2', 'uniE339': '6',
 'uniE624': '9', 'uniEA16': '5','uniF19A': '3', 'uniEE76': '0', 'uniF593': '4',
 'uniEFD4': '8'}



for index, key in enumerate(font_map):
    value = font_map[key]
    # hex() 函数用于将10进制整数转换为16进制，以字符串形式表示
    key = hex(key).replace('0', '&#')
    # 为防止对关系中没有相应的value导致报错，这里捕捉下异常
    try:
        # 这里用
        get_real_data = relation_table[value]
    except:
        get_real_data = ''
    if get_real_data != '':
        # 这里我们将字体文件中得到的编码字符和真是结果对应起来
        newmap[key] = get_real_data

print(newmap)