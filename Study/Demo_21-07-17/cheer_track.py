from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Facebook:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument('--disable-javascript')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.facebook_login_url = 'https://www.facebook.com/'
        self.driver = webdriver.Chrome(options=self.options)

    def facebook_login(self, url):
        self.driver.get(url)
        self.driver.find_element_by_id('email').send_keys("1584436652@qq.com")
        time.sleep(1)
        self.driver.find_element_by_id("pass").send_keys("lkt02230330")
        time.sleep(1)
        self.driver.find_element_by_name("login").click()


facebook = Facebook()
facebook.facebook_login(facebook.facebook_login_url)

