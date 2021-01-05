class Animal:
    def __init__(self):
        self.color='红色'
        pass
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs)
    pass

tigger=Animal()  # 实例化的过程会自动的调用__new__()方法去创建实例
# 在新式类中__new__()才是真正的实例化方法，为提供外壳制造出实例框架 然后__init__()进行丰满操作


