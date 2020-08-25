from fontTools.ttLib import TTFont


zt1 = TTFont("zt01.woff")

# wods列表中网页上按顺序打出来
words = ['B', '男', '王', '大', '专', 'M', '女', '吴', '硕', '赵', '黄', '李', '1', '8', '经', '2', '下', '本', '届', '5', '应', '科', '7', '中', '生', '6', 'E', '陈', '3', '以', '杨', 'A', '张', '4', '无', '0', '9', '验', '博', '技', '士', '校', '高', '刘', '周']

uni_list = zt1.getGlyphNames()[1:-1]

data_map = dict()
for index, i in enumerate(uni_list):
    temp = zt1["glyf"][i].coordinates
    x1, y1 = temp[0]
    x2, y2 = temp[1]
    new = (x2-x1, y2-y1)
    data_map[new] = words[index]
print(data_map)
