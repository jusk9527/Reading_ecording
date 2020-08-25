from fontTools.ttLib import TTFont

font1 = TTFont('zt01.woff')  # 打开本地字体文件01.ttf
uni_list = font1.getGlyphOrder()[2:]  # 前两个不算

print(uni_list)

# 输出信息如下

# ['uniE0D1', 'uniE0EB', 'uniE165', 'uniE39A', 'uniE3CD', 'uniE3DC', 'uniE4E6', 'uniE559', 'uniE5CE', 'uniE6FE', 'uniE74A', 'uniE811', 'uniE822', 'uniE90F', 'uniE925', 'uniE9A9', 'uniE9EB', 'uniEB2C', 'uniEC43', 'uniEC4C', 'uniEC7A', 'uniED1F', 'uniED8C', 'uniEDDB', 'uniEE02', 'uniEE6F', 'uniEF0E', 'uniEF58', 'uniEFD2', 'uniF0EB', 'uniF129', 'uniF1A3', 'uniF31A', 'uniF373', 'uniF3A5', 'uniF403', 'uniF459', 'uniF52A', 'uniF547', 'uniF56E', 'uniF58B', 'uniF5DB', 'uniF625', 'uniF832', 'uniF88E']


