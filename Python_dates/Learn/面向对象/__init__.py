from Learn.面向对象.demo_day7魔术方法 import Animal


class Animal(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    pass

    dog = Animal('旺财','white')
    # 对象的实例化
    print(dog)