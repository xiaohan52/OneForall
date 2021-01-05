# python中不使用def创建而使用lambda关键字创造的函数叫做匿名函数
# 其语法结构为:lambda 参数 参数 ： 执行代表达式，匿名函数自带一个return
test = lambda x,y:x+y
result = test(1,3)
print(result)

def test1(x,y):
    '''
    计算函数x+y的值
    :param x:
    :param y:
    :return: x+y
    '''
    X=x+y
    return X
    pass
result1=test1(1,3)
print(result1)
