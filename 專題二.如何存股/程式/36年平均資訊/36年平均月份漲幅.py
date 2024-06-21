import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

fn="EG27M01.csv"

data=pd.read_csv(fn)

print(data.head(20))

print(data.info())

#-----------------------------------------------------------------------------------------------------------資料預處理

#刪除不要的欄位
data=data.drop(data.columns[1:11],axis=1)

#刪除不要的欄位
data=data.drop(data.columns[2],axis=1)

#用來放入每月的漲幅大小
moon=[]

for i in range(439):
    
    if i>0:
        
        #算出每個月的漲幅大小
        moon.append((data.iloc[i][1]-data.iloc[i-1][1])*100/data.iloc[i-1][1])
    
    else:
        
        #第一筆沒有前一個資料可計算放入空值
        moon.append("NaN")

#設定新欄位(月漲幅)
data.insert(2,column="月漲幅(%)",value=moon)

print(data.head(20))

#創建新欄位month目的是將期間裡有用的月份資訊取出並轉成數字以利統計
#用.str可以對Series欄位裡的字串進行操作
data["month"]=data["期間"].str[5:].astype(int)

print(data)

#讓資料是以12為單位來計算，把多餘月份範圍刪除
data=data.drop(np.arange(7),axis=0)

print(data.head(20))

#------------------------------------------------------------------------------統計每月平均漲幅

#將每個月的平均漲幅統計出來
all_month_mean=data.groupby("month")["月漲幅(%)"].mean()

print(all_month_mean)

#------------------------------------------------------------------------------統計每月平均上漲機率

#用遮罩的概念將月漲幅>0的數據統計出來並把True跟False的資訊放到新欄位:漲幅>0 以利用groupby
data["漲幅>0"]=data["月漲幅(%)"]>0

#將每個月漲幅>0的次數統計出來
month=data.groupby("month")["漲幅>0"].sum()

print(month)

#算出每個月的平均上漲機率
month=month/36*100

print(month)

#-----------------------------------------------------------------------------------------------------------視覺化

#-----------------------------------------------------------------------------36年平均月份漲幅圖

x=all_month_mean.index

y=all_month_mean.values

plt.rcParams["font.family"]="Microsoft YaHei"

plt.figure(figsize=(40,20),facecolor="lightblue",dpi=300,edgecolor="r",linewidth=5)

#左上
plt.subplot(221)

#繪製水平線
plt.axhline(y=0, linewidth=4,color="c")

plt.plot(x,y,"r",label="月平均漲幅")

plt.title("36年平均月份漲幅",color="r",fontsize=20,pad=30)

plt.xlabel("月分",color="r",fontsize=20)

plt.ylabel("幅度(%)",rotation=35,color="r",labelpad=30,fontsize=20)

#顯示每年漲幅
plt.text(6,3,"36年平均年漲幅= %.2f%%" % all_month_mean.sum(),fontsize=25,color='r')

plt.legend(fontsize=20)

plt.xticks(np.arange(0, 13, 1))

#設定x、y的範圍
plt.axis([0,13,-4,4])

#顯示網格
plt.grid(color="lightblue")

#-----------------------------------------------------------------------------36年漲幅幅度密度分布圖

#plt.figure(figsize=(16,6),facecolor="lightblue")

#左下
plt.subplot(223)

#繪製漲幅幅度核密度估計圖
all_month_mean.plot.kde(label="漲幅密度")

plt.title('36年漲幅幅度密度分布圖',color="r",fontsize=16)

plt.xlabel('幅度 (%)',color="r",fontsize=16)

#labelpad功能:標籤與軸之間的間距
plt.ylabel('機率密度',rotation=0,labelpad=30,color="r",fontsize=16)

plt.axvline(x=0, linewidth=4,color="c")

plt.grid(color="lightblue")

plt.xticks(np.arange(-7, 7, 1))

plt.legend(fontsize=20)

#-----------------------------------------------------------------------------36年月份上漲機率圖

x1=month.index

y1=month.values

#右全
plt.subplot(122)

bars=plt.bar(x1,y1,width=0.5,label="漲幅大小")

#設定x、y軸範圍
plt.axis([0,13,0,100])

plt.xticks(np.arange(1,13,1))

plt.yticks(np.arange(0,110,10))

#畫水平線
plt.axhline(y=50,linewidth=2,color="purple",linestyle="--")

plt.title("36年月份上漲機率",color="r",fontsize=20,pad=30)

plt.xlabel("月份",fontsize=20,color="r")

plt.ylabel("機率",color="r",rotation=35,fontsize=20)

#將bars物件內容帶出
for bar in bars:
    
    h=bar.get_height()
    
    plt.text(bar.get_x(),h,"%.2f%%" % h,va="bottom",fontsize=15)

#用索引跟matplotlib的set_color方法將第二根長條圖改變顏色
bars[1].set_color("r")

plt.legend(fontsize=20)

#調整圖的比例
plt.tight_layout() 

plt.show()

























