import random

from time import sleep 

import csv

#匯入自訂函示，功能:爬取股票代號
from crawling_stock_symbol import stock_symbol

#匯入自訂函式，功能:分析ROE是否>15%
from analyze_ROE import ROE

#匯入自訂函式，功能:分析總負債佔比是否<70%且>20%
from analyze_total_liability import Total_liability

#匯入自訂函式，功能:分析自由現金流量是否>0
from analyze_free import Free

#匯入自訂函式，功能:分析本業佔比是否>80%
from analyze_main_business import Main_business

#匯入自訂函式，功能:分析現金股利是否有連續配發10年
from analyze_dividend import Dividend

#匯入自訂函式，功能:分析最近一年EPS>去年EPS or 前年EPS
from analyze_EPS import EPS

#爬取股票代號
number=stock_symbol()

#用來放入符合條件的股票代號
good_stock=[]

#用來放入有問題的股票代號
error_stock=[]

#用來放入問題股票的錯誤訊息
error_message=[]

#計算分析到第幾檔股票
count=0

for i in number:
    
    count+=1
    
    print("分析第",count,"檔")
    
    try:
        
        print("分析%s股票中....." % i)
        
#判斷ROE佔比區塊---------------------------------------------------------    
        
        #設定時間亂數
        random_sleep_time=random.uniform(3,5)
        
        print("分析ROE中~~~")
        
        #休息一下，降低網站負荷
        sleep(random_sleep_time)
        
        roe=ROE(i)
        
        #如果roe不符合就換下檔
        if roe<15:
            
            continue
            
#判斷現金股利區塊----------------------------------------------------------------
            
        print("分析現金股利中~~~")
         
        #休息一下，降低網站負荷
        sleep(random_sleep_time)
     
        dividend=Dividend(i)
            
        #如果dividend不符合我就換下檔
        if dividend<10:
                
            continue
            
#判斷本業佔比區塊----------------------------------------------------------------
            
        print("分析本業佔比中~~~")
            
        #休息一下，降低網站負荷
        sleep(random_sleep_time)

        main_business=Main_business(i)   
        
        #如果main_business不符合我就換下檔
        if main_business<80:
            
            continue
                
#判斷自由現金流量區塊------------------------------------------------------------
            
        print("分析自由現金流量中~~~")
    
        #休息一下，降低網站負荷
        sleep(random_sleep_time)

        free=Free(i)
        
        #如果free不符合我就換下檔
        if free<=0:
            
            continue
            
#判斷總負債佔比區塊--------------------------------------------------------------
    
        print("分析總負債佔比中~~~")

        #休息一下，降低網站負荷
        sleep(random_sleep_time)

        total_liability=Total_liability(i)
        
        #如果total_liability不符合我就換下檔
        if total_liability<20 or total_liability>70:

            continue
            
#判斷EPS區塊--------------------------------------------------------------------
            
        print("分析EPS中~~~")
        #休息一下，降低網站負荷
        sleep(random_sleep_time)
        
        eps=EPS(i)
        
        if eps>0:
            
            good_stock.append(i)
            
            print("good_stock=",good_stock)

#例外錯誤處理區塊-------------------------------------------------------------------            

    except Exception as e:
        
        print("%s地方錯誤,錯誤訊息: %s" % (i,e))
        
        error_stock.append(i)
        
        error_message.append(e)

#寫入區塊-----------------------------------------------------------------------

#把分析好的股票寫入good_stock.csv裡
with open("good_stock.csv","a",encoding="utf8",newline="") as file:
        
    write=csv.writer(file)
        
    write.writerow(good_stock)

#把有問題的股票代號跟錯誤訊息寫入error_stock.csv裡
with open("error_stock.csv","w",encoding="utf8") as file1:
            
    write1=csv.writer(file1)
    
    #分批寫入
    for j in range(len(error_stock)):
                
        write1.writerow([error_stock[j],error_message[j]])
    

    
            
            
