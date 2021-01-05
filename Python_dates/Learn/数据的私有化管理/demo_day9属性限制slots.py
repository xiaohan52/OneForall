# slots的作用  1.限制可以添加的实例属性   2.节约类型空间
class Student(object):
    __slots__ = ('name','age','score')

    def __str__(self):
        return '{}已经{}岁了'.format(self.name,self.age)

    pass


xw=Student()
xw.name='小王'
xw.age=20
xw.score = 96       # 一旦使用__slots__来对类属性进行限制，则该类无法动态添加属性
# 如果使用了__slots__那么下面的xw.__dict__将因为限制无法运行
# print(xw.__dict__)      # 所有可以添加的属性都在这个字典类型里面
print(xw)

# 在继承关系中，如果子列未使用__slots__，那么是不会继承父类的__slots__的
# 如果子类也声明了__slots__，那么子类的__slots__是子类的+父类的
class sunStudent(Student):

    pass
ln=sunStudent
ln.gender='男'
ln.pro='计算机'
print(ln.gender,ln.pro)