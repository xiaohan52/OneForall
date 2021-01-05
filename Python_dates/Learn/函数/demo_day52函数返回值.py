# 函数的返回值：当函数执行完之后会返回一个对象，如果在函数内部有return这个关键字，那就要返回实际的值，否则返回None
# 一个函数体内执行了return那就代表函数结束了

def Sum(a,b):
    sum = a + b
    return sum  # 将计算的结果返回给调用者
# re = Sum(10,20)
# print(re)   # 输出函数的返回值，返回到调用的地方

def calComputer(num):
    result = 0
    i = 1
    while i<=num:
        result+=1
        i+=1
        pass
    return result
pass

value = calComputer(10)
print(value)
print(type(value))

def returnTuple():
    '''
    返回元组类型的数据
    '''
    return 1,2,3
pass
A = returnTuple()
print(A)
print(type(A))