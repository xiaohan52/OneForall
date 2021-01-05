import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
'''
from matplotlib.font_manager import FontProperties   #显示中文，并指定字体
myfont=FontProperties(fname=r'C:/Windows/Fonts/simhei.ttf',size=14)
sns.set(font=myfont.get_name())
'''
data = pd.Series({"法师":0.197, '猎人':0.1557, '术士':0.1276,
                  '德鲁伊':'0.1126','牧师':0.1088, '盗贼':0.0938,
                 '圣骑士':0.0901, '萨满':0.0657, '战士':0.0488})
#print(data)
#plt.rcParams['figure.figsize'] = (8.0, 6.0)   #调整图片大小
#设置x,y轴比例为1：1，从而达到一个正的圆
plt.axes(aspect=1)
#plt.axis('equal')  # 设置x，y轴刻度一致，以使饼图成为圆形。
#labes标签参数,x是对应的数据列表,autopct显示每一个区域占的比例,explode突出显示某一块,shadow阴影是否显示
labes= data.index
explodes=[0.15 if i=='法师' else 0 for i in labes]
plt.pie(data, explode=explodes,labels=labes, autopct="%1.1f%%",
                                #colors=sns.color_palette("muted"),
                                startangle = 90,pctdistance = 0.6,
          textprops={'fontsize':14,'color':'black'},shadow=True)
plt.show()