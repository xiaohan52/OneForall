import numpy as np
import  matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
N=10
x=[3814.88,4037.45,4916.37,12187.98,14824.25,14885.01,16681.52,16990.99,22130.64,32198.689]

index=('Relativity','Summit','Lionsgate','Disney','Universal','Fox','Sony','Paramount','Warner Bros','Independent')
test1=plt.barh(y=index,height=0.3,color='red',width=x)#绘制水平柱状图

plt.title('2007-2011最赚钱电影公司排行')
plt.legend(["票房收入$m"])#图例展示
# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width+1, rect.get_y()+rect.get_height()/3, width, ha='center', va='bottom')
        rect.set_edgecolor('white')
add_labels(test1)


plt.show()