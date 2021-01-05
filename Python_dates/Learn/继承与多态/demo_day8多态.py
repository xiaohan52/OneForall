# 多态，定义时的类型和运行时的类型不一样
# 同一种行为，对于不同的子类对象都有不同的行为表现
# 多态有俩个前提: 1.必须存在继承 2.子类重写父类的方法

class Animal():
    '''
    父类[基类]
    '''
    def say_who(self):
        print('我是一个动物.......')
        pass
    pass
class Duck(Animal):
    '''
    鸭子类[派生类]
    '''
    def say_who(self):
        '''
        重写父类中的say_who方法
        :return:
        '''
        print('我是一只小黄鸭')
        pass
    pass
class Dog(Animal):
    '''
    小狗类[派生类]
    '''
    def say_who(self):
        print('我是一直哈巴狗')
        pass
    pass
class Cat(Animal):
    '''
    小猫类[派生类]
    '''
    def say_who(self):
        print('我是一只小花猫')
        pass
    pass
class Bird(Animal):
    def say_who(self):
        print('我是一只黄鹂鸟')
        pass
    pass


# 使用一个函数来统一调用多态中的某个方法
def commonInvoke(obj):
    '''
    统一调用的方法
    :param obj:
    :return:
    '''
    obj.say_who()
    pass

# Duck1 = Duck()
# Duck1.say_who()
# Dog1 = Dog()
# Dog1.say_who()
# Cat1 = Cat()
# Cat1.say_who()

listobj=[Dog(),Duck(),Cat(),Bird()]
for item in listobj:
    '''
    循环调用函数
    '''
    commonInvoke(item)
    pass

# 多态可以增加程序的灵活性，增加程序的拓展性