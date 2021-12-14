'''
@Time    : 2021/10/9 14:47
@Author  : LKT
@FileName: paypal.py
@Software: PyCharm
 
'''
import time
import re
import requests

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Paypal_Check(object):

    def __init__(self):
        self.options = Options()
        # self.options.add_argument('--start-maximized')
        self.options.add_argument('disable-infobars')  # 不显示Chrome正在受自动软件控制
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 3)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36',
        }
        # 登录url
        self.login_url = 'https://www.sandbox.paypal.com/signin'
        # 报告url
        self.report_url = 'https://business.sandbox.paypal.com/merchantdata/reportHome'

    def login(self):
        self.driver.get(self.login_url)
        self.wait.until(
            EC.presence_of_element_located((By.ID, "email"))).send_keys('sb-kiw4k8056759@business.example.com')
        time.sleep(1)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, 'btnNext'))).click()
        time.sleep(3)
        self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))).send_keys('I&9rW/_c')
        time.sleep(1)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, 'btnLogin'))).click()
        self.driver.get(self.report_url)
        print(self.driver.page_source)


    def get_csrf(self):
        try:
            response = requests.get(self.report_url, headers = self.headers).text
            print(response)
            csrf = re.findall(r'data-token=(.*?);', response, re.S)[0]
            return csrf
        except Exception as e:
            print('获取失败')
            raise e


    def get_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        return cookies

    def run(self):
        self.login()
        self.get_cookies()
        time.sleep(10)
        csrf = self.get_csrf()
        print(csrf)

pa = Paypal_Check()
pa.run()

