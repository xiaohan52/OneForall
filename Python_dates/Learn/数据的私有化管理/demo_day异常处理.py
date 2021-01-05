import exception
# except 在捕获错误的时候 只要根据具体的错误类型来捕获的
# print(dir(exception))
try:
    # print(b)   # 捕获错误代码
    li = [1,5,85]
    print(li[10])   # 通过下标去使用列表
    pass

# # 可以使用一个try多个except来捕获异常的类型
# except IndexError as msg:  # index 的错误类型
#     # 处理错误
#     print(msg)
#     pass
# except NameError as msg:   # name 的错误类型
#     print(msg)
#     pass

# 一个通吃的类型便是 Exception  当
except Exception as result:
    print(result)
    # 在此尽量去处理捕获的异常
    pass
# print('初次接触异常处理')
# print('hahahahaha')

def A(s):
    return 10/int(s)
    pass
def B(s):
    return A(s)/2
def main():
    try:
        A('0')
        pass
    except Exception as result:
        print(result)
    pass
main()  # 不需要在每个可能出错的地方去捕获，只要在合适的层次去捕获错误就可以了

# 异常抛出的机制  如果在运行时发生异常，解释器会查找相应的异常捕获类型，如果在当前没有找到，会将异常传递给上层的调用函数

# try:              可能出现错误的代码块
# except:           出现错误抛出的代码块
# else:             没有出现错误后抛出的代码块
# finally:          有没有错误都抛出的代码块


# 自定义一个异常类，需要直接或者间接的去继承Error或者Expection类
# 由开发者主动的抛出自定义异常，在python中使用raise关键字
class LeNumExcept(Exception):
    def __str__(self):
        return '[Error:]你输入的数字小于0,请输出大于0的数'
        pass
    pass

class LeNumExcept(Exception):
    def __str__(self):
        return '[Error:]你输入的数字小于0,请输出大于0的数'
        pass
    pass

    try:
        num = int(input('请输入一个数字'))
        if num<0:
            # raise抛出异常
              raise LeNumExcept(num)
        pass
    except LeNumExcept as e:
        print(e)   # 捕获异常
    else:
        print('没有异常')