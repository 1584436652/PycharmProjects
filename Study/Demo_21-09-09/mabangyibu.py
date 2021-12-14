from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


def download_file():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    # options.add_argument('hide-scrollbars')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("D:\Download\chromedriver_win32\chromedriver.exe", options = options)
    wait = WebDriverWait(driver, 3)
    driver.maximize_window()
    driver.get('https://900539.private.mabangerp.com/index.htm')
    wait.until(
        EC.presence_of_element_located((By.ID, "username"))).send_keys('13677395742')
    wait.until(
        EC.presence_of_element_located((By.ID, "password"))).send_keys('d6qE37SZ')
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#user-login > form > div >'
                                                   ' div.account-login > div:nth-child(6) > button'))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first-contents"]/li[3]'))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="M0010300MenuId"]/div[2]/div/a[1]'))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.ID, 'shopButton'))
    ).click()

    # 选取指定部门店铺
    count = 2
    for i in range(3, 14):
        shop = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/a'))
        )
        ActionChains(driver).move_to_element(shop).perform()
        stop = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/ul/li[3]/label'))
        )
        ActionChains(driver).move_to_element(stop).perform()
        while True:
            count += 1
            try:
                wait.until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/ul/li[{count}]/label'))
                )
                print(f'{i}---try{count}')
                continue
            except TimeoutException:
                stop1 = wait.until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/ul/li[{count-1}]/label'))
                )
                driver.execute_script("arguments[0].scrollIntoView();", stop1)
                break
        js_top = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js_top)
        ActionChains(driver).move_to_element(shop).perform()
        ActionChains(driver).move_to_element(stop).perform()
        print(count - 1)
        for j in range(3, count):
            text_first = wait.until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/ul/li[{j}]/label/span'))
            ).text
            if "一部" in text_first:
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="isHidden"]/li[{i}]/ul/li[{j}]/label/input'))
                ).click()
        count = 2


download_file()
