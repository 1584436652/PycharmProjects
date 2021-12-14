'''
@Time    : 2021/9/28 12:17
@Author  : LKT
@FileName: worldcould.py
@Software: PyCharm
 
'''

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud

jieba.setLogLevel(jieba.logging.INFO)
# 使用 jieba 进行分词
cut = jieba.cut("这个视频垃圾这个视频不错手机hello和hello china china china china very ")
string = ' '.join(cut)
print(string)

#读取背景图片

wc = WordCloud(font_path= r'C:\Windows\Fonts\simkai.ttf',  #使用系统中的字体，注意中文展示
   background_color='white',
   width=1000,
   height=800,
   )
# 根据文本生成词云
wc.generate_from_text(string)
process_word = WordCloud.process_text(wc,string)
print(process_word)
# 保存词云图片
wc.to_file('test.png') #保存图片
plt.imshow(wc)  #用plt显示图片
plt.axis('off') #不显示坐标轴
plt.show()
