# 使用元组推导式可以快速生成一个元组，他的表现形式和列表推导式相似，只是将[]修改为()
import random
randomnumber = (random.randint(10,100) for i in range(10))
print(randomnumber)
randomnumber = tuple(randomnumber)               # 使用tuple()来转换为元组，是用list()来转换为列表
print(randomnumber)

number = (i for i in range(3))
print(number.__next__())       # 输出第一个元素
print(number.__next__())       # 输出第二个元素
print(number.__next__())       # 输出第三个元素
number = tuple(number)         # 转换为元组
print("转换后:",number)

number1 = (i for i in range(4))     #生成生成器对象
for i in number1:                   #遍历生成器对象
    print(i,end="")                 #输出每个元素的值
print(tuple(number))                #转换为元组输出

