def Free(i):    
    
    import requests
    
    from bs4 import BeautifulSoup as bs
    
    #設定headers讓你看起來像個人!
    headers={
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
         }
    
    url=f"https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=CF_M_QUAR_ACC&STOCK_ID={i}"
        
    res=requests.get(url,headers=headers)
    
    res.encoding="utf8"
    
    soup=bs(res.text,"lxml")
    
    table_id=soup.find(id="tblFinDetail")
    
    #抓所有style="padding-left:4px"的標籤td 經過觀察只要抓前兩個
    td_style=table_id.find_all(style="padding-left:4px")
    
    #抓兄弟節點
    second_td=td_style[0].find_next_sibling("td").text
    
    #抓兄弟節點
    second_td1=td_style[1].find_next_sibling("td").text
    
    #business=營業活動之淨現金流入(出) 
    business=float(second_td.replace(",",""))
    
    #invest=投資活動之淨現金流入(出) 
    invest=float(second_td1.replace(",",""))
    
    #free=自由現金流量=營業活動之淨現金流入(出)+投資活動之淨現金流入(出)
    free=business+invest
    
    print(business)
    
    print(invest)
    
    print("自由現金流量: ",free)
    
    return free
    
    
    
    
    
    
    