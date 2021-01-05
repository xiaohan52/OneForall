class shenxian:
    def fly(self):
        print('神仙会飞')
    pass
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃子')
    pass
class SunWukong(shenxian,Monkey):   # 多继承，孙悟空既是神仙也是猴子
    pass
# 尝试调用方法，查看是否有子继承
# swk = SunWukong()
# swk.fly()
# swk.chitao()
'''
# 当多个父类中存在相同的方法的时候，会调用那个类中的方法呢
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass
class A(B,C):
    pass
a = A()
a.eat() # 在执行eat的方法时，顺序应该是查找方法往上查找，既是A的继承顺序
print(A.__mro__)  # __mro__魔术方法可以显示类的依次继承关系
'''

# 子类方法的重写，因为父类中的方法不能满足子类中的需要，那么子类就可以重写父类并且完善父类中的方法
class Dog():
    def __init__(self,name,color):
        self.name = name
        self.color = color
        pass
    def jiao(self):
        print('汪汪叫')
        pass
    pass

class kejiquan(Dog):
    def __init__(self,name,color):  # 属于重写父类的调用方法
        # 针对这种诉求，我们需要去调用父类的函数
        Dog.__init__(self,name,color)# 调用父类的方法 执行完毕就可以具备name和color的实例属性了
        super(kejiquan, self).__init__(name,color) # super 是自动找到父类并且调用其方法
        # 拓展其他的属性
        self.height = 90
        self.weight = 20
        pass
    def __str__(self):
        return '{}的颜色是{} 它的身高是{} 体重是{}'.format(self.name,self.color,self.height,self.weight)
    def jiao(self):
        print('柯基叫')
        super().jiao() # 调用父类的方法
        pass
    pass
keji = kejiquan('柯基犬','红色')
keji.jiao()
print(keji)
