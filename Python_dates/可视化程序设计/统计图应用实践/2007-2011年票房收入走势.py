import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 普通折线图
x = ['2007','2008','2009','2010','2011']
y = [16011,17814.4,22965.53,21979.481,22806.78]

plt.plot(x,y)

plt.legend(["票房收入$m"])

plt.show()