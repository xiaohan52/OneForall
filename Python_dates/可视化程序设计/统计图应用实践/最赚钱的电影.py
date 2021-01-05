import numpy as np
import  matplotlib.pyplot as plt
#设置横向条形图
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
N=20
x=[583,632.87,661,686.68,711.3,748.8,766.56,789.88,793.87,798.96,814.49,823.58,824.39,828.8,863.16,904,928.2,955,1203.11,2546.5]
index=('2012','Spider-Man 3','Pirates','Ice Age','Up ','Shrek Forever After','Indiana Jones','Harry Potter',
       'Pirates','Shrek the Third','The Dark Knight','Inception','Alice in Wonderland','Transformers','Toy Story 3','Harry',
       'Transformers','Harry3','Harry2','Avatar ')
test1=plt.barh(y=index,height=0.3,color='red',width=x)#绘制水平柱状图
plt.title('最赚钱的电影')
plt.legend(['最后收益$m'])#图例展示
# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width+1, rect.get_y()+rect.get_height()/3, width, ha='center', va='bottom')
        rect.set_edgecolor('white')
add_labels(test1)


plt.show()