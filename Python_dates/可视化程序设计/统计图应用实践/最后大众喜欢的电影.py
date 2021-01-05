import numpy as np
import  matplotlib.pyplot as plt

#设置横向条形图
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
N=5
x=[1328.11,1445.21,1587.76,1612.58,2783.5]
index=('Harry Potter and the Deathly Hallows Part 2','Spider-Man 3','Harry Potter and the Order of the Phoenix','Pirates of the Caribbean','Avatar ')
test1=plt.barh(y=index,height=0.3,color='red',width=x)#绘制水平柱状图
plt.title('大众最喜欢的电影')
plt.legend(["票房数$m"])#图例展示
# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width+1, rect.get_y()+rect.get_height()/3, width, ha='center', va='bottom')
        rect.set_edgecolor('white')
add_labels(test1)

plt.show()