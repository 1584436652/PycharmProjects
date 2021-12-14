from tkinter import *
import requests


url = input('sss')
def get_url(url):
    # url = inp1.get()
    res = requests.get(url=url).text
    txt.insert(END, res)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入


root = Tk()
root.geometry('460x240')
root.title('get百度')
lb1 = Label(root, text='百度url')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.6, relheight=0.1)
# 方法-直接调用 run1()
btn1 = Button(root, text='前往', command=get_url(url))
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root,)
txt.place(rely=0.6, relheight=0.6)
root.mainloop()





