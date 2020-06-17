# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df_head = df.head(10)
res_df_tail = df.head()

print(res_df_head)
# df.tail()就可以查看数据尾部的5行数据
print(res_df_tail)
# df.info()帮助我们一步摸清各列数据的类型，以及缺失情况：
print(df.info())
# 快速计算数值型数据的关键统计指标，像平均数、中位数、标准差等等
print(df.describe())

