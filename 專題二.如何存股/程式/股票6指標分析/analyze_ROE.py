def ROE(i):    
    
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
    
    #判斷ROE區塊-------------------------------------------------------
    
    #由於定位不了想要的td但上個td裡的div有id可以定位，因此先定位id
    div_id=soup.find(id="idDesc9")
    
    #找到div的父節點td
    div_parent=div_id.parent
    
    #定位父節點下個兄弟節點td
    second_td=div_parent.find_next_sibling("td").text
    
    #second_td內容是預估ROE的資料，選預估是怕公司公布時間不一
    ROE=float(second_td)
    
    print("ROE: ",ROE)
    
    return ROE
    
