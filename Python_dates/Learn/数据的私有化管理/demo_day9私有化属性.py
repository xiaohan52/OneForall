# 使用私有属性的场景
# 1.把特定的一个属性隐藏起来，不让类的外部进行直接调用
# 2.想要保护此属性，不想让属性的值随意的改变
# 3.保护这个属性，不想让派生类的[子类]去继承

class Person:
    __hobby='跳舞' # 类属性
    def __init__(self):
        self.__name='李四' # 加__便可以私有化,不可以在外部直接访问
        self.age=30
        pass
    def __str__(self):
        return '{}的年龄是{},爱好是{}'.format(self.__name,self.age,self.__hobby)
        pass
    def changeValue(self):
        Person.__hobby='唱歌'

    pass
class Student(Person):
    def printInfo(self):
        print(self.__name)  # 子类也不可以访问父类中的私有属性
    pass

# stu=Student()
# print(stu.__name)    # __name私有化属性也不可以在子类进行访问
# print(stu.__hobby)     # 不可以通过实例对象访问类属性
# print(Person.__hobby)  # 不可以直接访问私有化类属性
x1=Person()
# print(x1.__name)   # __name是私有化的属性，不可以在外部访问的
print(x1)
print('这是在类的内部修改私有化属性的结果后:')
x1.changeValue()
print(x1)