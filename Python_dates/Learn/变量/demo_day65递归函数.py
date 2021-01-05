# 求阶乘
# 循环的方式实现
def jiecheng(n):
    result = 1
    for item in range(1,n+1):
        result*=item
        pass
    return result

print('循环的方式实现10的阶乘{}'.format(jiecheng(10)))


# 递归必须自己调用自己，而且有一个明确的结束条件return
# 优点：逻辑简单，定义简单
# 缺点：防止内存消耗过多，容易栈溢出，甚至内存泄漏
# 递归函数方式来实现
def digui(n):
    '''
    递归函数实现参数
    :param n:
    :return:
    '''
    if n==1:
        return 1
    else:
        return n*digui(n-1)
    pass
print('递归函数实现10的阶乘{}'.format(digui(10)))

import os # 引入文件操作模块
def findfile(file_Path):
    listRs = os.listdir(file_Path) # 得到该路径下所有的文件夹
    for fileItem in listRs:
        full_Path=os.path.join(file_Path,fileItem) # 获取完整的文件路径
        if os.path.isdir(full_Path): # 判断是否是文件夹
            findfile(full_Path) # 如果是一个文件夹，再次去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

# 调用搜索文件夹对象
findfile('F:\\我的学习')

