def EPS(i):
    
    from selenium.webdriver.common.by import By 
    
    from selenium.webdriver import Chrome
    
    from selenium.webdriver.support.ui import Select
    
    from time import sleep
    
    driver=Chrome()
    
    driver.get(f"https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={i}")
    
    #等待網站開啟
    sleep(5)
    
    select=Select(driver.find_element(By.ID,"RPT_CAT"))
    
    #經觀察value值如下，一定是字串型態，這邊要找年度eps
    select.select_by_value("XX_M_YEAR")
    
    #讓網頁選單跳到年度
    sleep(5)
    
    #經觀察要抓的3筆資料不一樣的數字2,3,4
    num=["2","3","4"]
    
    #放入抓到的eps內容
    EPS=[]
    
    for i in num:
        
        #抓取eps內容
        eps=float(driver.find_element(By.XPATH,f"/html/body/table[2]/tbody/tr/td[3]/div/div/div/table/tbody/tr[8]/td[{i}]/nobr").text)
        
        EPS.append(eps)
    
    #查看內容是否正確    
    for i in range(3):
        
        print(EPS[i])
    
    #只要最近一年EPS>去年或前年EPS就符合條件
    if EPS[0]>EPS[1] or EPS[0]>EPS[2]:
        
        return 1
    
    else:
        
        return 0

        






