# for循环
# 语法特点：遍历操作，依次的取指令中的每个值
# for 临时变量in容器：
# 执行代码块
tags = '我是陈文星'    #字符串类型本身就是一个字符类型的集合
for item in tags:
    print(item)
    pass
# range 此函数可以生成一个数据集合列表
# range(起始：结束：步长)

sum = 0
for data in range(1,101):    #左包含右不包含
    sum += data    #求累加和
print('sum = %d' %sum)

print('——————for的使用——————')
for data in range(50,201):
    if data%2 == 0:
        print(data)
        pass
    else:
        print('%d是奇数'%data)

# break 和 continue
# break 代表中断，满足条件直接结束循环
# continue 结束本次循环，继续的进行下次循环，当continue的条件满足的时，本次循环剩下的语句不在执行了
sum = 0
for item in range(1,51):
    if sum > 100:
        break  # 退出循环体
        pass
    sum += item
    pass
# print('sum = %d' %sum)
print('continue的使用')
for item in range(1,51):
    if item%2 == 0:
        print('continue执行了！')
        continue
        print('continue执行了！')
        pass
    print(item)
    pass


