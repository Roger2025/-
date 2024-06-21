def Dividend(i):
    
    import requests
    
    from bs4 import BeautifulSoup as bs
    
    #設定headers讓你看起來像個人!
    headers={
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
         }
    
    url=f"https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID={i}"
         
    res=requests.get(url,headers=headers)
    
    res.encoding="utf8"
    
    soup=bs(res.text,"lxml")
    
    soup_id=soup.find(id="divDividendSumInfo")
    
    #先定位到資料所在的區塊id
    id_class=soup_id.find(class_="b1 p4_2 r0_10 row_mouse_over")
    
    class_tr=id_class.find_all("tr")
    
    #由於位置沒有東西定位而判斷這份資料是個表格形式應該不太會更動，因此選擇用索引來找位置
    tr_td=class_tr[3].find_all("td")
    
    #如果內容有+表示有連續配發，else則沒有連續配發
    if "+" in tr_td[7].text:
        
        #用索引抓出現金股利連續配發的位置內容，並把+刪除再轉成整數以利比較
        dividend=int(tr_td[7].text.replace("+",""))
        
        print("現金股利連續配發年數: ",dividend)
        
    else:
        
        dividend=0
    
    return dividend







