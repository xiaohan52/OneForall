class People:
    country='china'
# 类方法需要用@classmethod来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country # 通过类方法来访问类属性
        pass
    @classmethod
    def change_country(cls,data):
        cls.country=data # 在类方法中修改类属性的值
        pass

# 静态方法只要存放逻辑性的代码，本身和类以及实例对象没有交互
# 在静态方法中不会涉及到类中的方法和属性的操作
# 使数据资源能够得到充分的利用
    @staticmethod
    def getData():         # 一般情况下是不会通过实例对象去访问静态方法
        return People.country
        pass

    pass

# print(People.getData())

# print(People.get_country())  # 通过类对象直接去引用
# p=People()
# print('实例对象访问{}'.format(p.get_country()))  # 通过实例对象来直接访问

# People.change_country('japan')
# print(People.get_country())
import time
class TimeTest():
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second
        pass

    @staticmethod
    def showTime():
        return time.strftime('%H:%M:%S',time.localtime())
        pass
    pass

print(TimeTest.showTime())

