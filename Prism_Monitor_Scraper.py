#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import smtplib
import time


# In[2]:


url = 'https://prismplus.sg/collections/gaming-monitors/products/prism-w240'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'} # The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.
#get all data from website

def check_price():
    page = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(page.content,'html.parser')
    #title = soup.find(class='product-single__title').get_text()
    price = soup.find(id='ProductPrice-product-template').get_text()
    converted_price = float(price[12:15])
    print(converted_price)
    print(price.strip())
    

    if(converted_price < 150.0):
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()    #email comment when connecting to another server
    server.starttls()
    server.ehlo()
    
    server.login('okimsong7@gmail.com','rzgkhpiorzxowivn')
    
    subject = 'Price Fell Down!'
    body = 'check this link: https://prismplus.sg/collections/gaming-monitors/products/prism-w240'
    
    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(
        'okimsong7@gmail.com',
        'ksong.2016@socsc.smu.edu.sg',
        msg
    )
    print('email sent!')
    server.quit()
    
while(True):
    check_price()
    time.sleep(60)

