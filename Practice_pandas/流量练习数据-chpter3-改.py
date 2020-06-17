# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df_head = df.head()

print(res_df_head)


df["新增的列"] = range(1, len(df) + 1)
print(df.head())