# 列表的定义和其他的变量一样，创建列表时，可以使用=直接赋值 ，语法格式如下
# listname = [element1,element2,element3,...elementn]
# num = [7,84,57,31,94,25,85,83,27,95]
# # 可以创建空列表
# emptylist = []
# # 可以使用list()来将range()函数循环出来的结果转换为列表
# list(range(10,20,2))
# print(list(range(10,20,2)))
#
# # 同时可以使用del listname来进行列表的删除操作
# print(num,'这是列表删除前哦')
# del num
# print(num,'这是列表删除后哦')


# 输出每日一帖
import datetime             # 导入日期时间类
# 定义一个列表
mot = ["一个人无论走多远,映照的都是自己。心穷走多远都没用,让你日渐强大的不是走在路上的样子,而是向往飞上蓝天的丰满的心。",
       "恐惧自己受苦的人,已经因为自己的恐惧在受苦",
       "没有热忱，世间便无进步。",
       "强烈的信仰会赢取坚强的人，然后又使他们更坚强。",
       "如果不想做点事情，就不要想到达这个世界上的任何地方。",
       "风尘三尺剑，社稷一戎衣。",
       "即使心被炸得粉碎，血如井喷，我也依然安之若素，安之若素。"]
day = datetime.datetime.now().weekday()       #获取当前日期
print(mot[day])       #输出每日一贴


# 遍历列表，可以使用很多方法
# 1.直接使用for循环实现
#  for item in listname:
      # 输出item
print('   ','秋词')
verse = ["自古逢秋悲寂寥","我言秋日胜春朝","晴空一鹤排云上","便引诗情到碧霄"]
for a in verse :
    print(a)

# 2.使用for循环和enumerate()函数实现
#   for index,item in enumerate(listname):
      # 输出index 和 item
print('   ','秋词')
verse1 = ["自古逢秋悲寂寥","我言秋日胜春朝","晴空一鹤排云上","便引诗情到碧霄"]
for b,c in enumerate(verse1):
    print(b,c)

