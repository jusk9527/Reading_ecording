# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')
res_df_head = df.head()

df["支付转化率"] = df["支付转化率"].str.replace("%", '').astype(float)
print(df.head())


df["支付转化率"] = df["支付转化率"] / 100
print(df.head())


df["销售额"] = df["访客数"] * df["支付转化率"] * df["客单价"]
print(df.head())