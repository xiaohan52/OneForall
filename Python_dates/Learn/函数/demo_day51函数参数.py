# 参数的分类
# 默认参数[缺省参数] 可选参数 关键字参数
# 参数是函数为了实现特定的功能，进而为了得到实际功能所需要的数据

# 必选参数
def sum(a,b):        # a,b为形式参数，简称形参：只是意义上的一种参数，只是一种标记，在定义的时候是没有内存地址的
    sum = a + b
    print(sum)
    pass

# 函数的调用
sum(20,50)           # 20,50其实就是实际参数，简称实参，实参是占用内存的实实在在的数据

# 默认参数[缺省参数]
def sum1(a=10,b=20):       # 10，20其实就相当于是默认参数，如果函数内空缺的时候会自动调用默认参数
    sum1 = a + b
    print(sum1)
    pass
sum1(a=1)                # 如果未赋值，就会调用定义时候给的默认值

# 可选参数，其实相当于不定长的参数，当参数的个数不确定时使，比较灵活
def getComputer(*args):      # 一般都用args来表示可变参数
    '''
    计算累加和
    :param args:
    :return:
    '''
    result = 0
    for item in args:
        result += item
        pass

    print('result=%d'%result)
    pass
getComputer(1)            # 当元组中只有一个元素的时候，输出的时候会在后面加上一个,逗号，不然不会当作元组来处理
getComputer(1,2,3,4,5,6,7,8)

# 关键字参数，可变的参数  ** 来定义
# 在函数体内，参数关键字是字典类型，而且key的键是一个字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass
dictA={"name":"leo","age":35}
keyFunc(**dictA)           # 直接传递字典类型需要加**
keyFunc(name = 'peter',age = 15)
keyFunc()                 # 不进行传递也是可以的

def complexFunc(*args,**kwargs):          # 混合使用
    print(args)     # 输出的是元组类型
    print(kwargs)   # 输出的是字典类型
    pass
complexFunc(1,2,3,4,name = '陈文星')

# def TestMup(**kwargs,*args):            # 可选参数必须在关键字可选函数之前！
#     pass
#


