import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infile = r"C:\Users\MACHENIKE\Desktop\KSHCX\Hollywood_Movie_Dataset\2007.csv"
# infile2 = r"C:\Users\MACHENIKE\Desktop\KSHCX\Hollywood_Movie_Dataset\2008.csv"
# infile3 = r"C:\Users\MACHENIKE\Desktop\KSHCX\Hollywood_Movie_Dataset\2009.csv"
# infile4 = r"C:\Users\MACHENIKE\Desktop\KSHCX\Hollywood_Movie_Dataset\2010.csv"
# infile5 = r"C:\Users\MACHENIKE\Desktop\KSHCX\Hollywood_Movie_Dataset\2011.csv"
# outfile = r"C:\Users\MACHENIKE\Desktop\KSHCX\统计剧情分类排行.csv"
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
dataframe = pd.read_csv(infile,encoding = 'gb18030')
# 创建索引列表
data_Genre = dataframe.Genre
# print(data)

# def merge_list(L):
#     '''
#     将列表中相同的元素合并
#     '''
#     lenth = len(L)
#     for i in range(1, lenth):
#         for j in range(i):
#             if L[i] == {0} or L[j] == {0}:
#                 continue
#             x = L[i].union(L[j])
#             y = len(L[i]) + len(L[j])
#             if len(x) < y:
#                 L[i] = x
#                 L[j] = {0}
#
#     return [i for i in L if i != {0}]
#

data = pd.Series({"Action":0.237730061, 'Western':0.003067485, 'Horror':0.079754601,
                  'Romance':'0.039877301','Animation':0.076687117, 'Thriller':0.070552147,
                 'Comedy':0.257668712, 'Biography':0.016871166, 'Musical':0.009202454,
                  'Adventure':0.032208589,'Drama':0.156441718,'Fantasy':0.010736196,
                  'Documentary':0.006134969,'Sci-Fi':0.003067485})
plt.axes(aspect=1)
labes= data.index
explodes=[0.15 if i=='Action' else 0 for i in labes]
plt.pie(data, explode=explodes,labels=labes, autopct="%1.1f%%",
                                #colors=sns.color_palette("muted"),
                                startangle = 90,pctdistance = 0.6,
          textprops={'fontsize':14,'color':'black'},shadow=True)
plt.show()












plt.show()