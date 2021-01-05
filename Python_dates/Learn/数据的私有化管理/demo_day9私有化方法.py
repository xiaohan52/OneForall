# 有一些重要的方法不允许外部调用，为了防止子类的意外重写，把普通的方法设置为私有化方法，即在方法名前面加__

class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def run(self):
        self.__eat()
        print('奔跑')
        pass
    pass

class Bird(Animal):
    pass
bird1=Bird()
bird1.run()
# 可以在类的内部调用私有化方法，然后用类的内部的非私有化方法来进行在类的外部的私有化方法的调用