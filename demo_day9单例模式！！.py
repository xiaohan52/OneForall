# 单例模式是一种常用的软件设计模式 目的：确保某一个类只有一个实例存在
# 如果希望在某个系统中，某个类只有出现一个实例的时候，单例模式就出现了

# 创建一个单例对象 基于__new__()来实现

class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        # __new__()不能使用自身的__new__()方法，不然会造成一个深度的递归
        if not hasattr(cls,'_instance'):    # 如果不存在就会开始创建
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    pass


db1=DataBaseClass()
print(id(db1))
db2=DataBaseClass()
print(id(db2))


