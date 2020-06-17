# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df2 = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df2 = df2.head()
print(res_df2)
df2.to_csv("流量练习数据1.csv")


df3 = pd.read_excel('流量练习数据.xls')
res_df3 = df3.head()
print(res_df3)
df2.to_csv("流量练习数据2.xls")