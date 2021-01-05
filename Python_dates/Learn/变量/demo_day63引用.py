a=1
def func(x):
    print('x的地址:{}'.format(id(x)))
    x=2
    print('x修改后的地址:{}'.format(id(x)))
    pass
# 调用函数
print('a的地址:{}'.format(id(a)))
func(a)


# 可变类型
li=[]
def testRenc(parms):
    print(id(parms))
    li.append([1,2,3,4,5,6])
    pass
print(id(li))
testRenc(li)
print('外部的变量对象:{li}'.format(li))

# 在python中，所有的东西，都是对象，而每个对象都有一个地址
# 在函数调用的时候，实参的传递就是对象的引用