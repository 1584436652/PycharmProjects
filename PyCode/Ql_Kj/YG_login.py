from selenium import webdriver
import time
browser=webdriver.Chrome(executable_path='D:\PY\wrbdriver\chromedriver.exe')
browser.get('https://admin.yifengaf.cn/admin/index/login')
time.sleep(2)
browser.find_element_by_css_selector('#pd-form-username').send_keys('fywy66')
browser.find_element_by_css_selector('#pd-form-password').send_keys('qlkj9987')
# browser.find_element_by_css_selector('#btn btn-success btn-lg btn-block').sumbit()
browser.find_element_by_xpath('//*[@class="login-form"]/form/div[5]/button').click()   #点击登录
print(browser.get_cookies())


