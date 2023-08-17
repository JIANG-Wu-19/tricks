import pandas as pd
import wordcloud
import matplotlib.pyplot as plt
import matplotlib

from PIL import Image

# 读取数据
data = pd.read_excel('名单.xlsx')

# 输出人数
print('新生人数：', len(data))

# 统计数据
male = 0
female = 0
txt = ""
for i in range(len(data)):
    item = data.loc[i]

    if item['性别'] == "男":
        male += 1
    else:
        female += 1

    txt += item['籍贯'] + " "

# 绘制饼图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams["axes.unicode_minus"]=False

g=['男','女']
c=["b","y"]
t=[male,female]

plt.pie(t,labels=g,colors=c,autopct='%1.1f%%')

plt.title("新生男女比例")
# 输出图片
plt.savefig("新生男女比例.png")

# 绘制词云
w=wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path='C:\\Windows\\Fonts\\simfang.ttf')
w.generate(txt)
w.to_file('新生籍贯词云.png')
image=Image.open('新生籍贯词云.png')
image.show()
