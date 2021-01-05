# 列表的添加，修改，删除，以及统计计算

# + 可以运算，但是直接使用列表对象的append()方法要快一些 ：
# listname.append(obj)
verse1 = [1,2,3,4,5,6,7]
len(verse1)
print(verse1)
verse1.append('我是添加到末尾的元素哦')
len(verse1)
print(verse1)

# 列表对象的extend()方法实现，语法如下：
#  listname.extend(seq)
verse2 = [1,2,3,4,5,6]
verse3 = [7,8,9,10]
verse2.extend(verse3)
print(verse2)

# 列表元素中的修改只需要通过索引重新获取即可
verse4 = [1,2,3,4,5]
verse4[1] = '这是修改的第二个数哦'
print(verse4)

# 列表元素的删除可以根据索引或者元素值删除
verse5 = [1,2,3,4,5,6,7,8,9]
del verse5[-2]
print(verse5)

# 根据元素值删除可以使用列表的remove()
verse5.remove(5)
print(verse5)

#  对列表进行统计计算
#  python可以获取指定元素出现的次数 ， count()  语法格式为： listname.count(obj)
verse6 = [1,1,2,3,4,5,8,1,85,4,8,1,5,5,7,6,1,1,8,7,1]
num6 = verse6.count(1)
print(num6)

# 获取指定元素首次出现的下标   index()   语法格式为:  listname.index(obj)
verse7 = [0,1,2,3,4,5,6,7]
num7 = verse7.index(1)
print(num7)

# 获取数值列表的元素和   sum()   语法格式为   sum(listname[,start])
verse8 = [5,7,561,189,189,721,87,2,648]
num8 = sum(verse8)
print(num8)

# 对列表进行排序   sort()   语法格式为    listname.sort(key = None,reverse = False)
# Key 为比较键     reverse为可选参数，如果是ture就是降序，否则升序，默认升序
verse9 = [15,28,84,21,48,35,79,81,71,35,75]
verse9.sort()
print(verse9,'升序')
verse9.sort(reverse = True)
print(verse9,'降序')

char = ['cat','Angela','pet','Tom']
char.sort()       #区分大小写排序
print(char)
char.sort(key=str.lower)    #不区分大小写排序
print(char)

# 还可以使用一种内置函数sorted() 用完后原列表的元素顺序不变  语法格式为： sorted(iterable,key = None,reverse = False)
#    iterable:表示要进行排序的列表名称 key:比较键 reverse:可选参数，同上
verse10 = [99,98,85,74,69,91,81,86,79,60,51,48]    # 成绩列表
verse10_sx = sorted(verse10)
print('升序',verse10_sx)
verse10_jx = sorted(verse10,reverse=True)    # 降序排序
print('降序',verse10_jx)
print('原序列',verse10)


