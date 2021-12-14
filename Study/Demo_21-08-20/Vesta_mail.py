from selenium import webdriver
import time

driver = webdriver.Chrome('D:\google_map\chromedriver.exe')
driver.get('https://accounts.google.com')
# driver.find_element_by_id('identifierId').send_keys('chen1584436652@gmail.com')
# driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
# time.sleep(10)
driver.find_element_by_xpath('//*[@id="details-button"]').click()
driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/form/table/tbody/tr[2]/td/input').send_keys('admin')
driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/form/table/tbody/tr[4]/td/input').send_keys('shu88.cn20')
driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input').click()


