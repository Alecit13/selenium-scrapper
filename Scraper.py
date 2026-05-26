from selenium import webdriver
from selenium.webdriver.common import By
import time
import pandas as pd
driver=webdriver.Safari()
driver.get('https://news.ycombinator.com')
time.sleep(2)

lista=driver.find_elements(By.CLASS_NAME,'titleline')
age=driver.find_elements(By.CLASS_NAME,'age')


df=[]
for i, f in zip(lista[:10],age[:10]):
    titulo=(i.text)
    link=i.find_element(By.TAG_NAME,'a').get_attribute('href')
    fecha=f.get_attribute('title')
    df.append({'titulo':titulo,'link':link,'fecha':fecha})


driver.quit()
pd.DataFrame(df).to_csv('Datos/noticias.csv',index=False)
print('DataFrame guardado')
