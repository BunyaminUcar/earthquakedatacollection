from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests

driver=webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
driver.get("https://hasartespit.csb.gov.tr/")
print(driver.title)
time.sleep(20)
html=driver.page_source
soup = BeautifulSoup(html, 'html.parser')
  
kelime = []
for tr in soup.find_all('tr'):
    td_tags = tr.find_all('td')
    if len(td_tags) >= 9:
        kelime="".join(td_tags[0].text+"-"+td_tags[1].text+"-"+td_tags[2].text+"-"+td_tags[3].text +"-"+ td_tags[4].text +"-"+ td_tags[9].text)  
    for td in tr.find_all('td'):
        liste=[]
        if td.find('a'):
            for link in td.find_all('a'):           
                liste.append(link['href'])              
                for i, j in zip(liste, range(len(liste))):
                    if requests.get(i).status_code == 200:
                        dosya_adi1 = f"{kelime}-{j}.jpg".replace("'", "").replace("[", "").replace("]", "").replace(":", "")
                        with open(dosya_adi1, "wb") as f:
                            f.write(requests.get(i).content)   
                    else:
                        print("Fotoğraf Bulunamadı")                     
            print(liste)
            print(td_tags[4].text)
driver.quit()