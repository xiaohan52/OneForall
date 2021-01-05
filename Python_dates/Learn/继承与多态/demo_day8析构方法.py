# 析构方法相当于__del__()，对于一个方法，删除或者运行完毕时候需要销毁，称为析构方法，析构方法是一种魔术方法
class Animal(object):
    def __init__(self,name):
        self.name = name
        print('__init__()方法被调用')
        pass


    def __del__(self):
        '''
        来操作对象的释放，一旦释放完毕，对象便再也不可用
        :return:
        '''
        print('__del__()方法被调用')
        print('{}对象被销毁'.format(self.name))
        print('{}对象被彻底清理了，内存空间释放了'.format(self.name))
        pass


    pass

dog = Animal('旺财')
del dog   # 手动去清理删除dog这个对象
input('程序等待中.....')