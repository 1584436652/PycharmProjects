import keyboard  # 用于获取鼠标键盘输入
from PIL import ImageGrab  # 用于从剪切板获取图片并保存
from aip import AipOcr  # 用于识别图片中的文字并输出
import pyperclip  # 用于将识别出的文字放置到剪切板中方便直接粘贴
import time

if __name__ == '__main__':
    while True:
        # 按ctrl+c后才执行下面的语句
        keyboard.wait(hotkey='f1')
        keyboard.wait(hotkey='ctrl+c')
        # ctrl+c保存截图至剪切板， ImageGrab从剪切板读取图片
        time.sleep(1)
        img1 = ImageGrab.grabclipboard()
        # print(type(img))
        # 文件保存的名字
        img_path = '1.png'
        # 保存图片
        img1.save(img_path)
        # 百度api执行所需数据，运行需换成自己的APP_ID，API_KEY，SECRET_KEY
        APP_ID = '24595087'
        API_KEY = 'A9Dqch23gVtuPBfXmBeVGfoE'
        SECRET_KEY = 'qm5p1RwwzZBrgaXG5C4GbCKM2BMhgjwP'
        # 初始化AipOcr
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        with open(img_path, 'rb') as f:
            img2 = f.read()
        # print(type(img2))
        # 识别图片并返回结果
        result = aipOcr.basicAccurate(img2)
        data = ''
        # print(result)
        for r in result['words_result']:
            data = data + r['words'] + '\n'
        print(data)
        # 将文本复制到剪切板
        pyperclip.copy(data)
