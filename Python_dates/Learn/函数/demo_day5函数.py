# 在某一功能代码重复出现多次，但是为了提高编写的效率，把这些具有独立功能的代码块组织成为一个小模块，这就是函数
# 函数的定义：   def 函数名字(): 代码块              函数内容的第一行可以用字符串进行函数的说明

print('小星爱小涵%d'%520)
def printInfo():
    '''
    这个函数是用来打印小星爱小涵的组合
    '''
    # 函数代码块
    print('小星爱小涵%d' % 520)
    pass
printInfo()   # 函数的调用


# 函数的参数需要去定义
def printInfo1(name,height,weight,hobby,pro):
    '''
    输出人物的各项身体指标以及爱好
    '''
    print('%s的身高是%d'%(name,height))
    print('%s的体重是%d'%(name,weight))
    print('%s的爱好是%s'%(name,hobby))
    print('%s还喜欢%s'%(name,pro))
    pass
printInfo1('小涵涵',163,46,'打球','爱小星')