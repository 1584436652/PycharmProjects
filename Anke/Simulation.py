import win32api
import time
import lackey
import pyautogui
import schedule
import datetime


def rdo():
    #  调出RDO.exe
    win32api.ShellExecute(1, 'open',r'D:\\钉钉下载\\RDO(1)\\Remote Desktop Organizer v1.4.7\\RDO.exe','', '', 3)
    time.sleep(2)
    now = datetime.datetime.now()    # 获取当前时间
    current_date = time.strftime("%Y/%m/%d")    # 当前日期
    this_month_start = datetime.datetime(now.year, now.month, 1).strftime("%Y/%m/%d")   # 当月一号
    pyautogui.FAILSAFE = True  # 保护措施，避免失控
    pyautogui.PAUSE = 0.5  # 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒
    # pyautogui.doubleClick(232, 186, button='left')  # 滚动条下移
    # pyautogui.mouseDown(button='left')
    # pyautogui.mouseUp(button='left', x=229, y=192)
    i = 0
    j = 41
    while i < 360:
        i += 1
        j += 16
        if j > 860:
            j = 41
        if i == 58 or i == 117 or i == 176 or i == 235 or i == 294:
            pyautogui.moveTo(9, 55, duration=1)  # 控制鼠标移动
            pyautogui.click(clicks=1, button='left')  # 实现鼠标双击
            time.sleep(1)
            pyautogui.press('pagedown')    # 按键PageDown
            time.sleep(0.5)
            pyautogui.press('pagedown')
            continue
        else:
            try:
                pyautogui.moveTo(88,j, duration=1)  # 控制鼠标移动
                pyautogui.click(clicks=2)  # 实现鼠标双击账号
                # pyautogui.click(88,184,button='left',clicks=2,duration=0.2)  # 双击账号
                time.sleep(10)
                pyautogui.click(999,1023,button='right',clicks=1,duration=0.5)  # 右击屏幕底部
                time.sleep(2)
                pyautogui.press('s')  # 按s键，返回桌面
                time.sleep(2)
                lackey.doubleClick('photo/huohu1.png')  # 打开火狐浏览器
                time.sleep(6)
                pyautogui.click(690, 110, button='left', clicks=1,duration=0.5)    # 单击网址栏
                time.sleep(1)
                pyautogui.press('shift')
                time.sleep(1)
                # lackey.type('https://business.paypal.com/merchantdata/reportHome') # 输入报告页面网址
                pyautogui.typewrite(message='https://business.paypal.com/merchantdata/reportHome',interval=0.1)
                time.sleep(10)
                pyautogui.press('\n')  # 回车
                time.sleep(6)
                lackey.click('photo/dl.png')      # 登录账号
                time.sleep(15)
                lackey.click('photo/jiaoyi.png')   # 点击交易记录下载
                time.sleep(6)
                lackey.click('photo/xuanze.png')   # 选择所有交易
                time.sleep(1)
                # lackey.click('photo/suo.png')      # 点击所有记录
                pyautogui.click(863, 503, button='left', clicks=1, duration=0.5)
                time.sleep(1)
                lackey.click('photo/riqi.png')     # 选择日期
                time.sleep(1)
                lackey.click('photo/kaishi.png')   # 点击开始时间并输入(需改日期)
                lackey.type("2021/6/1")
                time.sleep(0.5)
                lackey.click('photo/fuzhu.png')
                time.sleep(0.5)
                lackey.click('photo/jieshu.png')   # 点击结束时间并输入(需改日期)
                lackey.type("2021/6/30")
                time.sleep(0.5)
                lackey.click('photo/fuzhu.png')
                time.sleep(0.5)
                pyautogui.click(1101,888,button='left',clicks=1,duration=0.2)   # 确认好时间点击
                time.sleep(0.5)
                lackey.click('photo/chuang.png')   # 创建报告
                time.sleep(5)
                lackey.click('photo/zhengyi.png')    # 点击争议
                time.sleep(5)
                lackey.click('photo/shijian.png')    # 选择事件
                time.sleep(0.5)
                # lackey.click('photo/souyoushijian.png')   # 所有事件
                pyautogui.click(853, 659, button='left', clicks=1, duration=0.2)
                time.sleep(0.5)
                lackey.click('photo/riqi.png')       # 选择日期
                time.sleep(1)
                lackey.click('photo/kaishi.png')     # 点击开始时间并输入(需改日期)
                lackey.type("2021/6/1")
                time.sleep(0.5)
                lackey.click('photo/fuzhu.png')
                time.sleep(0.5)
                lackey.click('photo/jieshu.png')     # 点击结束时间并输入(需改日期)
                lackey.type("2021/6/30")
                time.sleep(0.5)
                lackey.click('photo/fuzhu.png')
                time.sleep(0.5)
                pyautogui.click(1097, 975, button='left', clicks=1,duration=0.2)  # 确认好时间点击
                time.sleep(0.5)
                lackey.click('photo/shijian_csv.png')   # 选择格式
                time.sleep(0.5)
                # lackey.click('photo/excel.png')      # 选择excel格式
                pyautogui.click(1237, 730, button='left', clicks=1, duration=0.2)
                time.sleep(0.5)
                lackey.click('photo/chuang.png')   # 创建报告
                time.sleep(120)       # 这里时间大约休息3min
                lackey.click('photo/shuaxin.png')    # 点击事件报告刷新
                time.sleep(3)
                # lackey.click('photo/xiazai.png')     # 点击下载事件
                pyautogui.click(1580, 870, button='left', clicks=1, duration=0.2)  # 下载
                time.sleep(5)
                lackey.click('photo/queding.png')    # 跳出弹窗点击确定
                time.sleep(3)
                lackey.click('photo/jiaoyi.png')     # 创建交易记录时间较长,切换到交易记录下载
                time.sleep(5)
                lackey.click('photo/shuaxin.png')    # 点击刷新交易记录报告
                time.sleep(5)
                # lackey.click('photo/xiazai.png')   # 下载交易记录
                pyautogui.click(1585, 713, button='left', clicks=1, duration=0.2)  # 下载
                time.sleep(5)
                lackey.click('photo/queding.png')  # 跳出弹窗点击确定
                time.sleep(3)
            except Exception:
                print('第%d'%(i)+'个PP下载出错')
            finally:
                pyautogui.click(1893, 55, button='left', clicks=1, duration=0.5)  # 关闭浏览器
                time.sleep(3)
                pyautogui.click(347, 34, button='right', clicks=1, duration=0.5)  # 关闭账号
                pyautogui.click(394, 76, button='left', clicks=1, duration=0.5)


# rdo()
print("---1.需安装RDO,安装路径为——D:\\钉钉下载\\RDO(1)\\Remote Desktop Organizer v1.4.7\\RDO.exe---")
print("---2.Photo文件放入D盘根目录---""\n")
a = input("输入程序运行时间（格式如：21:00）：")
schedule.every().day.at(a).do(rdo)  # 每天在21:30时间点运行rdo函数s
while True:
    schedule.run_pending()  # 运行所有可运行的任务
