import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# 1、创建Chrome实例


# option = Options()
# option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Edge("D:\Download\edgedriver_win64\msedgedriver.exe",)
driver.set_window_size(1000, 1000)
# 2、driver.get方法将定位在给定的URL的网页 。
driver.get('https://accounts.google.com/')
driver.find_element_by_id('identifierId').send_keys('chen1584436652@gmail.com')
driver.find_element_by_id('//*[@id="identifierNext"]/div/button/span').click()
time.sleep(12)


