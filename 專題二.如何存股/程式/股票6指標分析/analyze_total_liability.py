def Total_liability(i):    
    
    import requests
    
    from bs4 import BeautifulSoup as bs
    
    #設定headers讓你看起來像個人!
    headers={
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
         }
    
    #設定網址
    url=f"https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={i}"
         
    #擷取url網址資料並回傳Response物件
    res=requests.get(url,headers=headers)
    
    #設定編碼
    res.encoding="utf8"
    
    #解析Response內容(必須是網頁格式的str)
    soup=bs(res.text,"lxml")
        
    #判斷負債總額區塊-------------------------------------------------------
      
    div_id=soup.find(id="idDesc50")  #經觀察id會變動要注意!
        
    div_parent=div_id.parent
        
    second_td=div_parent.find_next_sibling("td").text
        
    #second_td內容是總負債
    total_liability=float(second_td)
        
    print("總負債額: ",total_liability) 
        
    return total_liability