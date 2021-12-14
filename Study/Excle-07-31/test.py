import requests
import time
from openpyxl import workbook
from selenium import webdriver


def get_html(driver, page_data):
    global ws
    for page in range(1, page_data+1):
        data = []
        url = f'https://www.tokopedia.com/p/elektronik/alat-pendingin-ruangan/air-conditioner?page={page}'
        print("爬取第" + str(page) + '页ing')
        # driver.maximize_window()
        driver.get(url)
        time.sleep(3)
        move_first()
        data_list = driver.find_elements_by_xpath(
            '//*[@id="zeus-root"]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div[3]/div/a/div[2]/div[2]/span')
        for i in data_list:
            info = i.text.split('\n')
            # print(info)
            for j in info:
                data.append(j)
        print(len(data))
        # if len(data) == 75:
        for x in range(len(data)):
            ws.append([data[x]])
        print("第" + str(page) + '页爬取完成')
        print("\n")
        time.sleep(0.5)
        # else:
        #     print("第" + str(page) + '页数据缺失,没有爬取')
        #     print('\n')
        #     continue
    # print(data)
    # print(len(data))
    driver.quit()


def move_first():
    global driver
    js = "return action=document.body.scrollHeight"
    height = 0
    new_height = driver.execute_script(js)
    while height < new_height:
        for i in range(height, new_height, 100):
            driver.execute_script('window.scrollTo(0, {})'.format(i))
            time.sleep(0.01)
        height = new_height
        time.sleep(0.05)
        new_height = driver.execute_script(js)


def move_second():
    js = "var q=document.body.scrollTop=5000"
    driver.execute_script(js)


if __name__=='__main__':
    page = int(input("爬取的总页数Page=："))
    print("\n")
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['标题'])
    option = webdriver.ChromeOptions()
    option.add_experimental_option("useAutomationExtension", False)
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome("D:\Download\chromedriver_win32\chromedriver.exe", options=option)
    get_html(driver, page)
    wb.save('C:\\Users\\Administrator\\Desktop\\Indonesia.xlsx')
    print("已保存")
