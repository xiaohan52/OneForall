# 无参数，无返回值
def myprint():             # 一般用来提示信息打印
    print('-',* 20)
    pass

# 无参数，有返回值
def mycpu():               # 多用于在数据的采集
    '''
    获取cpu信息
    :return: info
    '''
    # 获取cpu信息
    return  0

# 有参数，无返回值
def set(a):                # 多用于在设置某些不需要返回值的参数类型
    return 0

# 有参数，有返回值
def cal(a,b):              # 一般是计算机形的，需要参数也需要返回结果
    c=a+b
    return c

