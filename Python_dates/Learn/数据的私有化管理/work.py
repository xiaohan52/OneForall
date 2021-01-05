# 1.python中new方法作用是什么
# 用来创建对象实例的，只有继承了object类才有这个方法
# 2.什么是单例模式，适用于什么场景？
# 要求一个类有且只有一个实例，并且提供了一个全局的访问点    日志插入logger的操作，网站计数器，权限验证模块
# 3.私有化方法和私有化属性在子类中能否继承？
# 不能
# 4.在python中什么是异常？
# 异常就是程序在执行的过程中发生的错误
# 5.python中是如何处理异常的
# try:
# except:
# else:
# finally:
# 6.__slots__属性的作用
# 限制属性的随意输入
# 节省资源空间
# 7.私有化类型的作用
# 保护数据，封装
# 8.在类外面是否能修改私有属性
# 不可以直接修改，通过方法来实现，还可以借助属性函数property去实现
# 9.如果一个类中，只有指定的属性或者方法能够被w外部修改，那么该如何限制外部修改
# 对数据进行私有化的设定

import types
class Person:
    def __init__(self,n,a):
        self.__name=n
        self.__age=a
        pass
    def __str__(self):
        return '{}的年龄是{}'.format(self.__name,self.__age)
    def getNameInfo(self):
        return self.__age
        pass
    def getAgeInfo(self):
        return self.__name
        pass
    def setName(self,name):
        self.__name=name
        pass
    def setAge(self,age):
        if age>0 and age<120:
            self.__age=age
        else:
            print('输入的数据不合法')
            pass
        pass

class Student:
    def __init__(self):
        self.name='张三'
        self.__score=90
        pass
    @property
    def name(self):
        return self.__name
        pass
    @name.setter
    def name(self,name):
        self.__name=name
        pass

    def get_score(self):
        return self.__score
        pass
    def set_score(self,score):
        self.__score=score
        pass

    score=property(get_score,set_score)

    def __str__(self):
        return '{}'
    def __call__(self, *args, **kwargs):
        print('{}的成绩是{}'.format(self.__name,self.__score))
        pass
    pass
# xw=Student()
# xw()   # 将实例对象以函数的形式去调用
# xw.name='李四'
# xw.score=88
# xw()

def run(self):
    print('小猫快跑')
class Animal:
    pass
Animal.color='白色'  # 绑定类属性
cat=Animal()
cat.run=types.MethodType(run,cat)         # 动态绑定
cat.run()
print(cat.color)





