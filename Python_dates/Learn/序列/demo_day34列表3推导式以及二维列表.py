# 列表推导式，可以快速生成列表，或者是根据某个列表生成条件来生成
import random
# 1.生成指定范围的数值列表，语法格式为：list = [Expression for var in range]
print('——————指定范围的列表——————')
randomnumber = [random.randint(10,100) for i in range(10)]
print('生成的随机数为:',randomnumber)

# 2.根据列表生成指定需求的列表，语法格式为: newlist = [Expression for var in list]
print('——————指定需求的列表——————')
price = [1200,5330,2988,6200,1998,8888]
sale = [int(x*0.5) for x in price]
print('原价格',price)
print('打折后的价格',sale)

# 3.从列表中选择符合条件的来组成新的列表，语法格式为: newlist = [Expression for var in list if condition]
print('——————符合之前条件的列表——————')
price1 = [1200,5330,2988,6200,1998,8888]
sale1 = [x for x in price1 if x>5000]
print('原价格',price1)
print('价格高于5000的',sale1)

# 二维列表，是由于列表元素可以是列表，列表因为这个原因可以套娃，类似二阶行列式
# 二维列表的创建 ：
# listname = [[1,2,3,4,5,6,7,8,9],[1,2,3,4],[1,2,3,4,5],[1,2,3,4]]

# 使用嵌套结构for循环来创建
arr = []
for i in range(4):      # 创建行的数目，同时使用range(4)来确定数组行数0，1，2，3
    arr.append([])
    for j in range(5):    # 创建列，同时确定数组列数0,1,2,3,4
        arr[i].append(j)
        pass
    pass
print(arr)

# 使用列表推导式创建
arr1 = [[j for j in range(5)] for i in range(4)]
print(arr1)


