from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import pandas as pd


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://medium.com/tag/technology")

Data=driver.page_source
allData=''.join(Data)


soup = BeautifulSoup(allData, 'html.parser')
Title=[]
Description=[]
Date=[]
Link=[0]*10
Innercontent=[]



Link[0]="https://medium.com/the-light-phone/buxton-school-goes-light-9ab46f290a7b" 
#Link[1]="https://medium.com/invisible-illness/learning-to-cope-with-estrangement-when-children-cancel-their-parents-914a4a80d2be"
#Link[2]="https://tomsmith585.medium.com/chatgpt-is-having-a-thomas-edison-moment-8342dd70d2bd"
#Link[3]="https://forge.medium.com/spotifys-year-end-lists-are-the-ultimate-personality-test-46b742e11a22"
#Link[4]="https://joulee.medium.com/why-your-team-needs-a-weekly-metrics-review-dcc9cce7ac3c"
#Link[5]="https://medium.com/@elliotgraebert/tyrion-lannister-and-the-7-habits-of-highly-effective-people-ee572a276064"
#Link[6]="https://zephoria.medium.com/what-if-failure-is-the-plan-2f219ea1cd62"
#Link[7]="https://efeng.medium.com/why-are-there-so-many-web3-startups-43a150379d52"
#Link[8]="https://chasten.medium.com/what-marriage-means-to-me-a6bdd72cffe1"
#Link[9]="https://nmoryl.com/leaving-san-francisco-2bf3663072cd"

print(Date)
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
    Innercontent.append(tem)
    break
print(Innercontent)

  
    
    