import numpy as np
import  matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x=np.random.rand(1000)+2
y=np.random.rand(1000)+3
plt.hist2d(x,y,bins=40)
plt.show()