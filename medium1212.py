from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32")
driver.get("")
data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')

y=3000
for i in range(10):
    driver.execute_script(f"window.scrollTo(0, {y} )") 
    y+=2000
    time.sleep(2)

A=soup.find_all('h2',class_="be ek kk kl km kn eo ko kp kq kr es ks kt ku kv ew kw kx ky kz fa la lb lc ld fe ff fg fh fj fk bj")
B=soup.find_all('p',class_="lf b fq ei ff lg fg fh lh fj fk iz bj")
c=soup.find_all('span',class_="bv b hw bx hj")    
    
data = driver.page_source

alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
Head = []
Link = []
Content = []
Date = []
para = []
print(Date)
for k in range(len(A)):
    Head.append(A[k].string)
for j in range(len(B)):
    para.append(B[j].string)
for lnk in Link:
    driver.get(lnk)
    Data1=driver.page_source
    allData1=''.join(Data1)


    soup = BeautifulSoup(allData1, 'html.parser')
    M=soup.find_all('div',id="root")
    print(M)
    tem=""
    for j in M:
        tem+=j.get_text()
    Content.append(tem)


 