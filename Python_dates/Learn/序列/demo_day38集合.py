# 集合类似于列表list[] 元组tuple(),其语法结构为： setname = {element1,element2}
set1 = {'水瓶座','射手座','双鱼座','双子座'}
print(set1)
# 同时在python中，可以使用set()函数来将列表，元组，等其他可迭代对象转换为集合，其语法格式如下：setname = set(iteration)
set1 = set(set1)

# 可以使用add()方法来向集合中添加元素，也可以使用del命令删除整个集合，亦或是使用pop(),remove()方法来删除一个元素，或者clear()来清空元素
set1.add('金牛座')             # add()添加元素
print(set1)
set1.remove('金牛座')          # remove()移除指定元素
print(set1)
set1.pop()                    # pop()移除第一个栈里面的元素
print(set1)
set1.clear()                  # .clear()来清空集合
print(set1)

#  集合的交集，并集，差集的运算
#  交集运算时使用&，并集运算时使用|，差集运算时使用-，对称差集运算时使用^

python = set(['绮梦','冷伊','香凝','紫萱'])            # 保存选择python的学生姓名
c = set(['冷伊','圣四','零语','香凝'])                 # 保存选择c的学生姓名
print('选择python的学生有:',python)                   # 输出选择python的学生姓名
print('选择c的学生有:',c)                             # 输出选择c的学生姓名
print('交集运算:',python & c)                         # 输出两个课程都选的学生姓名
print('并集运算:',python | c)                         # 输出参与了选课的学生姓名
print('差集运算:',python - c)                         # 输出选了python但是没有选c的学生姓名

