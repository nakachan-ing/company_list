from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
import pandas as pd
import time


keyword = '広告代理店'
url = 'https://itp.ne.jp/'


browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get(url)
time.sleep(3)
print("iタウンページにアクセスしました")


element = browser.find_element_by_xpath('//*[@id="keyword-suggest"]/input')
element.clear()
time.sleep(3)
element.send_keys(keyword)


search = browser.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div/div[2]/form/button')
time.sleep(3)
search.click()
print("検索します")


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
elements_num = range(1,len(elements)-1)

for (element,num) in zip(elements, elements_num):
    company_list.append(element.find_element_by_class_name('m-article-card__header__title__link').text)
    try:
        url_list.append(element.find_element_by_xpath(f'//*[@id="__layout"]/div/article/div[3]/div/div/main/ul/li[{num}]/div/div/article/div/div/div/a').get_attribute('href'))
    except NoSuchElementException:
        url_list.append('urlが存在しません')


result ={
    'company_list': company_list,
    'URL_link': url_list
}


df = pd.DataFrame(result)


df.to_csv('result.csv', index=False, encoding='utf-8')


# df_result = pd.read_csv('result.csv')
