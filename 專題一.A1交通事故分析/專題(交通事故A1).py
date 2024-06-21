import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
fn="111年度A1交通事故資料.csv"
data=pd.read_csv(fn,encoding="utf8")
plt.rcParams["font.family"]="Microsoft YaHei"

#-------------------------------------------------------------------------------------天氣圖

'''#用counter來統計各類型天氣的數量
weather=Counter(data["天候名稱"])

#查看weather有哪些天氣狀況
print(weather)

#使用畫布設定數值
plt.figure(figsize=(6,6),dpi=1000,facecolor="#FFFFBB",edgecolor="r",linewidth=5)

#設定適合天氣的顏色
colors=["#FFFF33","#99FFFF","#003377","#AAAAAA","#33CCFF","#E8CCFF"]

#把統計出來的天氣狀況設成標籤以利畫圖
labels=['晴','雨','陰','霧或煙','暴雨','強風']

#使用串列生成式來帶出統計完的天氣狀況數量
size=[weather[item] for item in labels]

#調整字擠在一起的部分
explode=[0,0,0,0,0.24,0.42]

#繪製圓餅圖
plt.pie(size,labels=labels,explode=explode,colors=colors,autopct="%1.1f%%",
        labeldistance=1.2)

#確保畫出來是圓形
plt.axis("equal")

#設定標籤
plt.title("事故天候狀況")

#存檔
plt.savefig('事故天氣圖.png')

#顯示圖表
plt.show()'''

#-------------------------------------------------------------------------------------道路類別圖

'''plt.figure(figsize=(12,6),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

#統計道路類別由大排到小並繪製住柱狀圖
data["道路類別-第1當事者-名稱"].value_counts().plot(kind="bar")

plt.title("道路類別-第1當事者-名稱")

plt.xlabel("道路類別")

plt.ylabel("數量")

#調整x軸標籤為水平
plt.xticks(rotation=0)

plt.savefig('事故發生道路類別.png')

plt.show()'''

#-------------------------------------------------------------------------------------事故位置and事故類型圖

'''plt.figure(figsize=(12,6),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

#設定子圖第一張(左)
plt.subplot(121)

#統計(事故位置子類別名稱)
location=data["事故位置子類別名稱"].value_counts()

#前5大占比設定為location_top5
location_top5=location.head(5)

#把前5大後面的項目做加總
location_other_sum=location[5:].sum()

#把加總數值設成其他新增到location_top5
location_top5["(其他)"]=location_other_sum

#繪製圓餅圖
plt.pie(location_top5.values,labels=location_top5.index,autopct="%1.1f%%",explode=(0.03,0,0,0,0,0))

plt.title("事故位置子類別名稱")

plt.axis("equal")

#設定子圖第二張(右)
plt.subplot(122)

#統計(事故類型及型態子類別名稱)
type_=data["事故類型及型態子類別名稱"].value_counts()

#前7大占比設定為location_top5
type_top7=type_.head(7)

#把前7大後面的項目做加總
type_other_sum=type_[7:].sum()

#把加總數值設成其他新增到type_top7
type_top7["(其他)"]=type_other_sum

#繪製圓餅圖
plt.pie(type_top7.values,labels=type_top7.index,autopct="%1.1f%%",explode=(0.05,0,0,0,0,0,0,0))

plt.axis("equal")

plt.title("事故類型及型態子類別名稱")

#讓圖的邊框收得比較完整 減少空白的地方
plt.savefig('事故類型及型態子類別名稱圓餅圖.png',bbox_inches='tight')

plt.show()'''

#-------------------------------------------------------------------------------------肇事原因圖

'''#統計(肇因研判子類別名稱-主要)
cause=data["肇因研判子類別名稱-主要"].value_counts()

#前5大占比設定為cause_top5
cause_top5=cause.head(5)

#把前5大後面的項目做加總
cause_other_sum=cause[5:].sum()

#把加總數值設成其他新增到cause_top5
cause_top5["(其他)"]=cause_other_sum

plt.figure(figsize=(10,7),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

plt.pie(cause_top5.values,labels=cause_top5.index,autopct="%1.1f%%",explode=(0.05,0,0,0,0,0))

plt.axis("equal")

plt.title("肇因研判子類別名稱-主要")

plt.legend()

plt.savefig('肇因研判子類別名稱-主要圓餅圖.png',bbox_inches='tight')

plt.show()'''

#-------------------------------------------------------------------------------------事故發生年齡圖

'''#使用遮罩將不合理的值(0,-1,111)的值塞選掉
mask_data=data[(data["當事者事故發生時年齡"]>0)&(data["當事者事故發生時年齡"]!=111)]

plt.figure(figsize=(16,10),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

plt.subplot(211)

#統計(當事者事故發生時年齡)在把標籤排序成由小到大並繪製長條圖
mask_data["當事者事故發生時年齡"].value_counts().sort_index().plot(kind="bar")

plt.title("當事者事故發生時年齡")

plt.xlabel("年齡")

plt.ylabel('數量')

#設定Y軸刻度位置和標籤 
plt.yticks(np.arange(0,110,10),(labels for labels in range(0,110,10)))

#繪製箭頭指向18歲(事故件數最多)
plt.annotate("18歲事故\n件數最高",xy=(17,93),
             xytext=(3,80),
             arrowprops={"width":1,
                         "headlength":8,
                         "headwidth":10,
                         "facecolor":"y",
                         "shrink":0.05},
             fontsize=20,color="#CC00CC")

#繪製箭頭指向28歲
plt.annotate("28歲",xy=(27,73),
             xytext=(30,80),
             arrowprops={"width":1,
                         "headlength":8,
                         "headwidth":10,
                         "facecolor":"y",
                         "shrink":0.05},
             fontsize=20,color="#CC00CC")

#使用遮罩把18~28歲區間的row保留起來(事故最多的區間)
mask_data1=data[(data["當事者事故發生時年齡"]>=18)&(data["當事者事故發生時年齡"]<=28)]

plt.subplot(212)

#把塞選好的mask_data1做分組取值並將值排序成由大到小取前三繪製出長條圖
mask_data1.groupby("肇因研判子類別名稱-主要").size().sort_values(ascending=False).head(3).plot(kind="bar")

plt.title("18~28歲前三大肇因")

plt.xticks(fontsize=13,rotation=0)

plt.xlabel("肇因")

plt.ylabel("數量")

#調整圖的比例
plt.tight_layout()

plt.savefig('當事者事故發生時年齡 and 18~28歲前三大肇因.png',bbox_inches='tight')

plt.show()'''

#-------------------------------------------------------------------------------------事故車種圖

'''data=data.dropna(subset=["當事者區分-類別-大類別名稱-車種"])

plt.figure(figsize=(12,6),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

data["當事者區分-類別-大類別名稱-車種"].value_counts().plot(kind="bar")

plt.xticks(rotation=90)

plt.title("當事者區分-類別-大類別名稱-車種")

plt.xlabel("車種")

plt.ylabel("事故數量")

plt.savefig('當事者區分-類別-大類別名稱-車種.png',bbox_inches='tight')

plt.show()'''

#-------------------------------------------------------------------------------------縣市事故圖

#因沒找到縣市人口百分比的檔案，在這邊手動創建一份
dic={"臺中市政府警察局":12.1,"新北市政府警察局":17.17,"高雄市政府警察局":11.73,
     "桃園市政府警察局":9.81,"臺南市政府警察局":7.96,"彰化縣警察局":5.35,
     "屏東縣政府警察局":3.43,"雲林縣警察局":2.85,"國道公路警察局":0,
     "臺北市政府警察局":10.66,"嘉義縣警察局":2.1,"苗栗縣警察局":2.3,
     "新竹縣政府警察局":2.5,"宜蘭縣政府警察局":1.93,"花蓮縣警察局":1.37,
     "其他":0}

#轉換成一維
data_=pd.Series(dic)

#把資料*10以利畫圖的呈現，在這邊想看出人口百分比跟事件的關西來了解六都跟鄉下誰比較會發生事故
data_=data_*10

#統計(處理單位名稱警局層)
city_counts=data["處理單位名稱警局層"].value_counts()

#設定畫布
plt.figure(figsize=(12,6),dpi=1000,facecolor="#99FFFF",edgecolor="r",linewidth=5)

#前15大占比設定為top_cities15
top_cities15=city_counts.head(15)

#把前15大後面的項目做加總
other_cities_sum=city_counts[15:].sum()

#把加總數值設成其他新增到top_cities15
top_cities15.loc["其他"]=other_cities_sum

#計算數據的長度
n_groups=len(data_)

#產生一組跟data_長度依樣的序列
index=np.arange(n_groups)

#設定長條圖寬度
bar_width=0.35

#繪製長條圖 
plt.bar(index,top_cities15.values,bar_width,label="案件数",align="center")

#繪製長條圖，位置在原先位置往後移一個寬度(剛設好的bar_width)
plt.bar(index+bar_width,data_.values,bar_width,color='r',label="人口%x10",align="center")

#繪製箭頭
plt.annotate('''把屏東縣人口佔比*3\n=3.43%s*3\n=10.29%s\n\n把屏東事件數%s*3\n=%d件\n\n可看出鄉下事故件數用%s來看>六都''' 
             % ("%","%",top_cities15["屏東縣政府警察局"],top_cities15["屏東縣政府警察局"]*3,"%"),
             xy=(6,top_cities15["屏東縣政府警察局"]),
             xytext=(8,320),
             arrowprops={"width":1,
                         "headlength":8,
                         "headwidth":10,
                         "facecolor":"y",
                         "shrink":0.05},
             fontsize=12,color="#CC00CC")

plt.title('處理單位名稱警局層')

plt.xlabel('縣市')

plt.ylabel('數量')

#設定Y軸刻度位置和標籤 
plt.yticks(np.arange(0,600,50),(labels for labels in range(0,600,50)))

#設定標籤位置為兩個長條圖的中間
plt.xticks(index+bar_width/2,data_.index,rotation=45,fontsize=15)

#在圖表添加圖例
plt.legend()

#調整圖的比例
plt.tight_layout() 

plt.savefig('處理單位名稱警局層.png',bbox_inches='tight')

plt.show()

#-------------------------------------------------------------------------------------end

























