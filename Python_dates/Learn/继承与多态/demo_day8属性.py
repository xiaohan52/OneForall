# 属性分为类属性和实例属性

# 类属性，就是类对象所拥有的属性
class Student:
    name='李明' # 属于类属性，就是student的属性
    def __init__(self,age):   # 属于实例属性
        '''
        实例属性
        :param age:年龄
        '''
        self.age = age
        pass

    pass
lm = Student(18)
print(lm.name)   # 通过实例对象去访问类属性
lm.name='刘德华'  # 通过实例对象对类属性进行修改是不可以的
Student.name='陈文星' # 通过类对象对类属性进行修改，可以，而且所有对此类对象的引用都全部修改
print(lm.age)
print('**********通过类对象student去访问类属性*************')
print(Student.name)
# print(Student.age)                # 只有类属性才可以使用类名.的方式去访问
# 类属性是可以被类对象和实例对象去访问的
# 实例属性只能通过实例对象去访问
# 实例属性在每个实例中独有一份，而类属性则是所有实例对象共有一份
# 所有实例对象和类对象指针指向同一  类对象



