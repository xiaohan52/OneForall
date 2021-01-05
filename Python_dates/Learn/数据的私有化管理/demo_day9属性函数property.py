class Person(object):
    def __init__(self):
        self.__age=18   # 定义一个私有化属性
        pass
    def get_age(self):
        return self.__age
        pass
    def set_age(self,age):
        if age <= 0:
            print('年龄不可以小于0')
        else:
            self.__age = age
            pass
        pass
    # 定义一个类属性，实现通过直接访问属性的形式去访问私有的属性
    age = property(get_age,set_age)  # 方法一，直接定义property函数来进行访问

# 方法二，通过使用property装饰器来修饰私有化的属性，添加属性标志后，使用getter方法
    @property # 用装饰器修饰 添加属性标志 提供一个getter方法
    def age(self):
        return self.__age
        pass
    @age.setter  # 提供了一个setter方法可以使用
    def age(self,parms):
        if parms<=0:
            print('年龄不可以小于0')
        else:
            self.__age=parms
            pass
        pass

    pass
p1=Person()
print(p1.age)
p1.age = 25
print(p1.get_age())

