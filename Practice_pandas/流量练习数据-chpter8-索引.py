# utf-8
import pandas as pd
import xlrd
# engine是使用的分析引擎，读取csv文件一般指定python避免中文和编码造成的报错
df = pd.read_csv("./流量练习数据.csv", engine="python",encoding='GB18030')

# 行索引
res_df_hang = df.iloc[:13,:]
print(res_df_hang)




# 列索引
res_df_lie = df.iloc[:,[0,4]]
print(res_df_lie)


# 行列教程索引
res_df = df.iloc[13:18,0:4]
print(res_df)



