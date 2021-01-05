import numpy as np
import  matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


N=20
x=[731.3,748.8,768,786.56,798.96,823.58,836.3,886.68,890.87,934,939.88,955,961,999.49,1024.39,1043.87,1063.16,1123.20,1328.11,2783.50]

# index=np.arange(N)
index = ('Shrek Forever After','2012','Indiana','Shrek the Third','Inception','Transfor','Ice Age','Spider-Man 3','Harry','Potter','Harry','Harry Potter','Pirates','The Dark Knight','Alice in Wonderland','"Pirates','Toy Story 3','Transformers','Harry Potter','Avatar')
test1=plt.barh(y=index,height=0.3,color='black',width=x)#绘制水平柱状图

plt.title('2007-2011世界电影票房排行榜')
plt.legend(["电影票房$m"])#图例展示
# 添加数据标签 就是矩形上面的数值

def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width+1, rect.get_y()+rect.get_height()/3, width, ha='center', va='bottom')
        rect.set_edgecolor('white')
add_labels(test1)

plt.show()