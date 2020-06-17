# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df_head = df.head()


# 单列值
print(df["客单价"])



# 多列值
print(df[["流量来源","访客数","支付转化率"]])



# 修改

df['旧列名'] =  "某个值或者某列值"