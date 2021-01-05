import types        # 添加方法的库
def dymicMethod(self):
    print('{}的体重是{}kg,在{}上学'.format(self.name,self.weight,Student.school))
    pass
@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    pass
    def __str__(self):
        return '{}今天{}岁了'.format(self.name,self.age)
    pass
print('绑定类方法')

print('************类方法执行结束*************')

print('--------------给类对象添加属性----------------')
Student.school = '武汉轻工大学'     # 动态添加类属性


cwx = Student('陈文星',20)
cwx.weight = 50  # 动态添加的属性
cwx.printInfo=types.MethodType(dymicMethod,cwx)  # 动态的绑定方法
# print(cwx)
# print(cwx.weight)
cwx.printInfo()  # 调用动态绑定的方法
print('-------------------------')

xph = Student('谢佩涵',20)
print(xph)
try:
    print(xph.weight)
    pass
except Exception as msg:
    print(msg)
pass


print(xph.school)

