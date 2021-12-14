from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random

options = webdriver.ChromeOptions()
# download.default_directory：设置下载路径，profile.default_content_settings.popups：设置为 0 禁止弹出窗口
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\Selenium_Yg\\chuhao'}
options.add_experimental_option('prefs', prefs)
browser=webdriver.Chrome(executable_path='D:\PY\wrbdriver\chromedriver.exe',chrome_options=options)
browser.get('https://admin.yifengaf.cn/admin/notice/index?ref=addtabs')      # 域名
browser.maximize_window()
browser.find_element_by_css_selector('#pd-form-username').send_keys('fywy66')    # 账号
time.sleep(1)
browser.find_element_by_css_selector('#pd-form-password').send_keys('qlkj2058889')  # 密码
time.sleep(1)
# browser.find_element_by_css_selector('#btn btn-success btn-lg btn-block').sumbit()
browser.find_element_by_xpath('//*[@class="login-form"]/form/div[5]/button').click()   #点击登录
time.sleep(2)
browser.find_element_by_xpath('//*[@class="slimScrollDiv"]/section/ul/li[6]/a').click()  # 点击订单结算
time.sleep(1)
# browser.find_element_by_xpath('//*[@class="slimScrollDiv"]/section/ul/li[6]/ul/li[1]/a').click()     # 点击账单明细
browser.find_element_by_xpath('//a[@pinyin="dingdanmingxi"]').click()
time.sleep(1)
d =[
"圣元书文","书点趣阁","亢龙文学","苍南文舍",
"无尘书斋","盘龙书舍","清风文社","龙吟精选",
"灵锋阅读","帝江书坊","起源小书","仙尊品读",
"东皇书刊","无极书社","鸿轩书局","轩辕书刊",
"雪鹰文学","光耀文选","君子文摘","苍龙书社",
"云天秘阁","九霄书舍"
]
for i in d:
    browser.find_element_by_xpath("//a[@data-title='切换账号']").click()   # 切换账号
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_id("layui-layer-iframe1"))  # 切换iframe表单
    time.sleep(3)
    browser.find_element_by_id("nickname").send_keys(i)   # 书名
    time.sleep(1)
    browser.find_element_by_xpath('//button[@class="btn btn-success"]').click()  # 提交账号
    time.sleep(1)
    browser.find_element_by_xpath('//a[@data-button-index="2"]').click()   # 切换账号
    time.sleep(1)
    browser.switch_to.default_content()  # 将表单切回到最外层
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("//body/div[1]/div[1]/div[2]/iframe"))   # 切换iframe表单
    time.sleep(2)
    # 点击支付状态
    browser.find_element_by_xpath('//select[@class="form-control"]').click()
    time.sleep(1)
    #点击已支付
    browser.find_element_by_xpath('//option[@value="1"]').click()
    # msg=["选择",'//select[@class="form-control"]']
    # try:
    #     a = Select(browser.find_element_by_xpath(msg[1]))
    # except:
    #     print("没有找到{0}".format(msg[0]))
    #     browser.quit()
    # else:
    #     list1=[]
    #     for select in a.options:
    #         string=select.text
    #         rep_str=string.replace(" ","").replace("\n","")  #清理数据，此行可删
    #         list1.append(rep_str)
    #     list_random=random.randint(1,len(list1))
    #     print("成功选择{0},选择第{1}个".format(msg[1],list_random))
    #     a.select_by_visible_text(list1[list_random-1])
    time.sleep(1)
    # browser.find_element_by_id("orders.finishtime").click()   # 点击完成时间
    a = browser.find_element_by_xpath('//input[@placeholder="完成时间"]')
    browser.execute_script("arguments[0].click();", a)
    time.sleep(1)
    browser.find_element_by_id("orders.finishtime").send_keys('2019-11-21 00:00:00 - 2019-11-21 23:59:59')   # 输入完成时间
    time.sleep(1)
    b = browser.find_element_by_xpath('//div[@class="panel panel-default panel-intro"]/div/div/div/div/div/div/form/fieldset/div/div[7]/div/button')#点击提交
    browser.execute_script("arguments[0].click();",b)
    # 点击导出
    browser.find_element_by_id('toolbar').click()
    time.sleep(1)
    browser.switch_to.default_content()  # 将表单切回到最外层
    time.sleep(1)




