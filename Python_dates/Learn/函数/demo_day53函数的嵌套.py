# 函数的嵌套
def fun1():
    print('——————fun1代码执行——————')
    print('——————fun1代码块——————')
    print('——————fun1代码结束——————')
    pass

def fun2():
    print('——————fun2代码执行——————')
    fun1()
    print('——————fun2代码结束——————')
    pass
fun2()         # 调用函数fun2()

# 函数的分类：根据函数的返回值和函数的参数
