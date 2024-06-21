import csv

import pandas as pd

import matplotlib.pyplot as plt

fn="臺灣採購經理人指數(pmi及nmi).csv"

data=pd.read_csv(fn)

print(data.info())

print(data.head(15))

data=data.tail(60)

print(data)

#------------------------------------------------------------------------------資料清理

#轉換成日期格式
data["Date"]=pd.to_datetime(data["Date"],format="%Y%m")

#設置索引為日期
data.set_index("Date",inplace=True)

print(data)

#------------------------------------------------------------------------------視覺化

plt.rcParams["font.family"]="Microsoft YaHei"

plt.figure(figsize=(16,6),dpi=300,facecolor="#99FFFF",edgecolor="r",linewidth=5)

plt.plot(data["PMI"].index,data["PMI"])

plt.title("近5年製造業採購經理人指數(PMI)")

plt.xlabel("時間軸")

plt.ylabel("指數")

plt.axhline(y=50,color='r',linestyle='--')

plt.text(data.index[59],51,"榮枯線",color="r")

plt.show()









