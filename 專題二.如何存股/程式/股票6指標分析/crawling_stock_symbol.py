def stock_symbol():
    
    import requests
    
    from bs4 import BeautifulSoup as bs
    
    import re
    
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
    
    url="https://stock.wespai.com/p/3752"
    
    res=requests.get(url,headers=headers)
    
    if res.status_code==200:
        
        soup=bs(res.text,"lxml")
        
        id_=soup.find(id="example")
        
        tbody=id_.find("tbody")
        
        tr_all=tbody.find_all("tr")
        
        #用串列生成式生成符合正規表達式規則的股票號碼 正規表達式目的:排除6位數的號碼
        stock_number=[tr.find("td").text for tr in tr_all if re.findall(r"^\d{4}$",tr.find("td").text)]
        
        print(stock_number)
            
        print(len(stock_number))   
    
        return stock_number
    
    else:
        
        print("Response回傳錯誤，狀態碼為:%d" % res.status_code)
        
        return res.status_code

