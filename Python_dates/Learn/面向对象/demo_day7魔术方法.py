class Animal(object):          # object属性
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    pass

    def __str__(self):         #
        '''
        打印对象 自定义对象 是内容格式的
        :return:
        '''
        return '我的名字是%s,我的颜色是%s'%(self.name,self.colour)

    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法 每调用一次 就会生成一个新的对象 cls就是class的缩写
        场景：可以控制创建对象的一些属性限定 经常用来做单例模式的时候使用
        :param args:
        :param kwargs:
        '''
        return object.__new__(cls)  # 在这里真正创建对象实例
        pass

# __new__和__init__函数的区别
# __new__类的实例化方法，必须要返回该实例，否则对象就创建不成功
# __init__用来做数据类型的初始化工作，也认为是实例的构造方法，接受类的实例self并且对其进行构造
# __new__至少有一个参数是cls代表要实例化的类，此参数可自动提供
# __new__的执行是要早于__init__函数的

dog = Animal('旺财','white')
print(dog)



