import requests
import time
from openpyxl import workbook
from selenium import webdriver


def get_html(driver):
    url = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news' \
          '_8758433490525774593%22%7D&n_type=0&p_from=1'        # driver.maximize_window()
    driver.get(url)
    # move_first()
    time.sleep(0.5)
    # time.sleep(0.5)
    while True:
        # data = []
        try:
            data_list = driver.find_elements_by_xpath(
                '//div[@class="xcp-item"]')
            for i in data_list:
                name = i.find_elements_by_xpath('//h5[@class="user-bar-uname"]')
                comment = i.find_elements_by_xpath('//span[@class="type-text"]')
                count = i.find_elements_by_xpath('//span[@class="like-text"]')
            for names, comments, counts in zip(name, comment, count):
                name_text = names.text
                comment_text = comments.text
                count_text = counts.text
                # data.append(name_text)
                # data.append(comment_text)
                # data.append(count_text)
                # print(name_text, comment_text, count_text)
                item = dict(
                    账户名称 = name_text,
                    评论信息 = comment_text,
                    点赞数量 = count_text
                )
                print(item)
        except:
               print('dao except')
        finally:
            lass_page = driver.find_elements_by_xpath('//*[@id="commentModule"]/div[2]/div/div[2]/span')
            for i in lass_page:
                lass_page_text = i.text
            # print(lass_page_text)
            if lass_page_text == "没有更多啦":
                print("没有更多啦")
                break
            else:
                print('加载更多评论')
                driver.find_element_by_xpath('//*[@id="commentModule"]/div[2]/div/div[2]/span').click()
                time.sleep(0.3)

            # driver.quit()

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


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("useAutomationExtension", False)
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome("D:\Download\chromedriver_win32\chromedriver.exe", options=option)
    get_html(driver)
