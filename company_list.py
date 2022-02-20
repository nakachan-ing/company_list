#!/usr/bin/env python
# coding: shift-jis

# In[1]:


#get_ipython().system('pip install selenium')


# In[2]:


#get_ipython().system('pip install beautifulsoup4')


# In[59]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
import pandas as pd
import time


# In[60]:


keyword= input('キーワードを入力してください: ')


# In[61]:


keyword_area= input('エリアを入力してください:')


# In[62]:


url = 'https://itp.ne.jp/'


# In[63]:


browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get(url)
# r = requests.get(url)
time.sleep(3)
print("iタウンページにアクセスしました")


# In[64]:


element_word = browser.find_element_by_xpath('//*[@id="keyword-suggest"]/input')
element_word.clear()
time.sleep(3)
element_word.send_keys(keyword)

element_area = browser.find_element_by_xpath('//*[@id="area-suggest"]/input')
element_area.clear()
time.sleep(3)
element_area.send_keys(keyword_area)

print("【キーワード】:%s 【エリア】:%sで検索します" %(keyword, keyword_area))

search = browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div/div[2]/form/button')
time.sleep(3)
search.click()

# In[83]:


company_list = []
url_list = []
i = 1
i_max = 5

while i <= i_max:
    
    
    if browser.find_elements_by_xpath('//*[@id="__layout"]/div/article/div[3]/div/div/main/div/button') ==[]:
        i = i + 1
    else:
        next_page = browser.find_element_by_xpath('//*[@id="__layout"]/div/article/div[3]/div/div/main/div/button')
        next_page.click()
        time.sleep(1)
    i += 1
        
elements = browser.find_elements_by_class_name('o-result-article-list__item')
elements_num = range(1,len(elements)+1)

for (element,num) in zip(elements, elements_num):
    company_list.append(element.find_element_by_class_name('m-article-card__header__title__link').text)  
    try:
        url_list.append(element.find_element_by_xpath(f'//*[@id="__layout"]/div/article/div[3]/div/div/main/ul/li[{num}]/div/div/article/div/div/div/a').get_attribute('href'))
    except NoSuchElementException:
        url_list.append('urlが存在しません')

print(company_list)
print(url_list)

# In[84]:


result ={
    'company_list': company_list,
    'URL_link': url_list
}


# In[85]:


df = pd.DataFrame(result)
print(df)

# In[86]:


df.to_csv(f'{keyword}_{keyword_area}.csv', index=False, encoding='shift-jis')


# In[87]:


# df_result = pd.read_csv(f'{keyword}.csv')

