# 模块的制作说明

__all__=['add','diff']      # 如果使用了此魔术变量，那么也意味着这个变量中的元素会被 from xxx import * 会被导入，否则无法导入
def add(x,y):
    '''
    相加的函数
    :return:
    '''
    return x+y
    pass
def diff(x,y):
    return x-y
    pass
def printInfo():
    return '这是我自定义模块里面的一个方法'


# 可以使用以下代码使的模块内进行测试运行而模块外不可见
if __name__=='__main__':
    res = add(2,8)
    print(res)
