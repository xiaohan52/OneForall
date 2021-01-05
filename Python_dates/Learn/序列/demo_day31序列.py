# 在python重，序列就是一组按照顺序排列的值【数据集合】
# 存在3种内置的序列类型：
# 字符串，列表，元组
# 优点：可以进行索引和切片的操作
# 特征：第一个正索引为0，指向的是左端，第一个索引为负数的时候，指向的是右端

verse = ["自古逢秋悲寂寥","我言秋日胜春朝","晴空一鹤排云上","便引诗情到碧霄"]
print(verse[2])     # 输出第三个元素
print(verse[-1])    # 输出最后一个元素

# 切片，是操作访问序列种元素的一种方法，他可以访问一定范围内的元素，而且通过切片操作可以生成一个新的序列
# sname[start:end:step]
# 名称[开始位置：步长：截至位置]
verse1 = [1,2,3,4,5,6,7,8,9,10]
print(verse1[1:6:2])
print(verse1[0:2])   #步长若是省略则也要省略前面的:,此时步长默认为1
print(verse1[6:9:2])

print(verse + verse1)    # 序列是可以通过使用+运算符来相加的(相同类型)
print(verse * 3)     # 序列也可以通过*来进行多次使用，例如输出

# 在序列种，使用数字n乘以一个序列会生成新的序列，而且新序列的内容会是原来的n次，例如下面的代码
emptylist = [None] * 5
print(emptylist)

# 同时可以通过使用in关键字来检查某个元素是否包含元素，语法格式为
# value in sequence
verse2 = [9,8,7,6,5,4,3,2,1]
print(9 in verse2)
print(5 not in verse2,10 in verse2)    # 同时也有not in 来判断是否不在此序列中


#  python中提供了内置函数来计算序列的长度，最大值以及最小值
#  len()  max()  min()

num1 = [7,84,6,51,81,58,34,75,25,94]
print('序列num1的长度为',len(num1))
print('序列num1的最大值为',max(num1))
print('序列num1的最小值为',min(num1))

#  python中的内置函数除了以上还有   list(序列转换列表)  str(转换字符串)  sum(计算和)  sorted(排序)  reversed(反序)  enumerate(组合)
