from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)
# Read the whole text.
text = open(path.join(d, 'his.txt'), encoding='utf-8').read()
import jieba

# 结巴分词
wordlist = jieba.cut(text, cut_all=True)  # 将文本分割，返回列表
wl = " ".join(wordlist)  # 将列表拼接为以空格为间断的字符串
print(wl)  # 输出分词之后的txt
coloring = np.array(Image.open(path.join(d, "3.png")))  # 定义词频背景
# 设置停用词
# stopwords = set(STOPWORDS)
# stopwords.add("said")
# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white",  # 背景色
               max_words=1000,  # 最大显示单词数
               mask=coloring,  # 自定义显示的效果图
               max_font_size=50,  # 频率最大单词字体大小
               random_state=42,  #
               font_path='simhei.ttf'  # 字体
               )  # 设置一张词云图对象
wc.generate(wl)
# create coloring from image
image_colors = ImageColorGenerator(coloring)
# show
# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
wc.to_file(r'.\xxx.png')
plt.imshow(wc, interpolation="bilinear")  # 设置图片
plt.axis("off")  # 取消图片X,Y轴
plt.figure()  # 创建一个图表画布
plt.show()  # 显示图片
