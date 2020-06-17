# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df_head = df.head()

df["日期"] = "2019-8-3"
print(df.head())

df["日期"] = pd.to_datetime(df["日期"])
print(df["日期"].head())



res_df_datatime = pd.to_datetime('2019-12-31') - pd.to_datetime(df["日期"])
print(res_df_datatime)