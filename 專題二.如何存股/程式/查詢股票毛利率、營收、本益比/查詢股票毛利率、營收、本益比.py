import pandas as pd

import matplotlib.pyplot as plt

import os

from time import sleep

print("可查詢上市櫃公司特定的財務資訊並且幫您畫圖儲存到桌面~")

while True:

    try:

        number=input("請輸入要查詢的股票代號 可連續輸入查詢以(空白)做間隔: ")
    
        number=number.split()
        
        print(number)
        
        for item in number:
        
            url=f"https://histock.tw/stock/{item}/%E5%88%A9%E6%BD%A4%E6%AF%94%E7%8E%87"
            
            data=pd.read_html(url)
            
            print(len(data))
            
            print(data[0])
            
            print(type(data[0]))
#--------------------------------------------------------------------------------------------------------------------資料清理           
            #用.set_index()來把指定column的資料變為索引值
            data=data[0].set_index("年度/季別")
            
            print(data)
            
            #對行進行逆向取值，實現將行做逆向排序
            data=data.iloc[::-1]
            
            #也可寫data["毛利率"]=data["毛利率"].replace("%","",regex=True)
            #將data["毛利率"]裡右側的%刪除並將數據從str轉成浮點數以利畫圖
            data["毛利率"]=data["毛利率"].str.rstrip("%").astype(float)
            
            print(data)
            
            #降低網站負荷
            sleep(3)
            
            url1=f"https://histock.tw/stock/{item}/%E6%90%8D%E7%9B%8A%E8%A1%A8"
            
            data1=pd.read_html(url1)
            
            data1=data1[0]
            
            print(len(data1))
            
            print(data1)
            
            data1=data1.set_index("年度/季別")
            
            print(data1)
            
            data1=data1.iloc[::-1]
            
            print(data1)
            
            #降低網站負荷
            sleep(3)
            
            url2=f"https://histock.tw/stock/{item}/%E6%9C%AC%E7%9B%8A%E6%AF%94"

            data2=pd.read_html(url2)

            data2=data2[0]
            
            print(data2.columns)
            
            #使用串列生成式來生成所有(本益比)的欄位
            pe_columns=[i for i in data2.columns if "本益比" in i]

            #將(本益比)的5個欄位合併成一個
            combined_pe_series=pd.concat([data2[i] for i in pe_columns])

            print(combined_pe_series)

            #使用串列生成式來生成所有(年度/月份)的欄位
            year_columns=[j for j in data2.columns if "年度/月份" in j]

            #將(年度/月份)的5個欄位合併成一個
            combined_year_series=pd.concat([data2[j] for j in year_columns])

            #設定一維的index
            combined_pe_series.index=combined_year_series

            print(combined_pe_series)

            #將資料倒轉
            combined_pe_series=combined_pe_series[::-1]
            
            #算出5年平均本益比
            mean=combined_pe_series.mean()
            
#--------------------------------------------------------------------------------------------------------------------視覺化

#-----------------------------------------------------------------------------------------------毛利率圖

            plt.rcParams["font.family"]="Microsoft YaHei"
            
            plt.figure(figsize=(24,8),facecolor="lightblue",dpi=300,edgecolor="r",linewidth=5)
            
            plt.subplot(221)
            
            plt.bar(data.index,data["毛利率"])
            
            plt.title(item+" 毛利率")
            
            plt.ylabel("單位%")
            
#-----------------------------------------------------------------------------------------------營收圖
            
            plt.subplot(223)
            
            plt.bar(data1.index,data1["營收"])
            
            plt.title(item+" 營收")
            
            plt.ylabel("元")
            
#-----------------------------------------------------------------------------------------------本益比河流圖

            plt.subplot(122)
            
            plt.plot(combined_pe_series.index,combined_pe_series.values,label="本益比河流圖")

            plt.title(f"{item} 近5年平均本益比")

            plt.xlabel("年度/月份")

            plt.ylabel("本益比")

            plt.xticks(rotation=90)

            plt.legend(fontsize=17)
            
            plt.axhline(mean,color="r",linestyle="--")
            
            plt.text(-6,mean,"5年平均",color='r',fontsize=12,rotation=90,va="center")

            plt.tight_layout()
            
#---------------------------------------------------------------------------------------------------------------------創建檔案區塊
            
            #假如沒有item+"_file"的資料夾就創建一個
            if not os.path.exists(item+"_file"):
                
                os.makedirs(item+"_file")
            
            #設定一個拼接路徑
            image_path=os.path.join(item+"_file",f"{item}_毛利率營收資料.png")
            
            #保存到剛設定的拼接路徑中
            plt.savefig(image_path)  
            
            plt.show()
            
        answer=input("是否要繼續查詢 輸入(Y)繼續 輸入其他跳出: ")
            
        if answer.upper()!="Y":
                
            print("停止查詢~")
                
            break
            
    except Exception as e:
        
        print("錯誤訊息:",e)
        
        
        
                    

        
        
        
        
        
        
        
        
        
        
