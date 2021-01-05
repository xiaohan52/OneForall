#   ————————————————局部变量————————————————
# 局部变量就是在函数内部定义的变量，其作用域仅仅在函数内部
# 不同的函数可以定义相同的局部变量(名字，数字类型)
# 局部变量的作用：为了临时的保存数据，需要在函数中定义来进行存储
# ————————————————————全局变量————————————————————
# 全局变量的区别就是作用域的不同
# 当全局变量和局部变量出现重复定义，程序会优先执行函数内部的变量，及局部变量
# 如果在函数的内部想要对函数进行修改，必须使用global来进行声明
pro = '计算机信息管理'
name = '吴老师'
def printInfo():
    name='prter'
    print('{}'.format(name))
    pass
def TestMethod():
    print(name)
    pass

def changeleGlobal():
    '''
    要修改全局变量
    :return:
    '''
    global pro
    pro='摸鱼技巧'
    pass

print('修改前：'+pro)
changeleGlobal()
print('修改后：'+pro)

