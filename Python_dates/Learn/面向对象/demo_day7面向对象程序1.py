# 类的对象以及定义和使用

# class ClassName:
#     '类的帮助信息'        # 类文档字符串
#     statement           # 类体  主要由类的变量，方法和属性等定义语句组成

class Geese:
    '''大雁类'''

    def __init__(self, beak, wing, claw):  # 构造方法
        print('我是大雁类，我具有以下特征:')
        print(beak)
        print(wing)
        print(claw)

    def fly(self, state):
        print(state)

    '''******************调用方法********************'''


beak_1 = '喙的基部较高，长度和头部的长度几乎相同'  # 喙的特征
wing_1 = '翅膀长而且尖'  # 翅膀的特征
claw_1 = '爪子是蹼形的'  # 爪子的特征


# wildGoose = Geese(beak_1,wing_1,claw_1)            # 创建大雁类的实例
# wildGoose.fly('我飞行的时候，一会排成个人字，一会排成个一字')  # 调用实例方法

class Geese1:
    '''雁类'''
    neck = '脖子较高'
    wing = '振翅频率高'
    leg = '腿位于身体的中心支点，行走自如'
    number = 0

    def __init__(self):  # 构造方法
        Geese1.number += 1  # 编号加一
        print('\n 我是第' + str(Geese1.number) + '只大雁，我属于雁类！我有如下特征:')
        print(Geese1.wing)
        print(Geese1.leg)
        print(Geese1.neck)


# 创建4个雁类的对象
list1 = []
for i in range(4):
    list1.append(Geese1())
    print('一共有' + str(Geese1.number) + '只大雁')

# 访问限制   可以在属性或方法前面添加_for  __for _for_
#  _for 以单下划线开头的表示protected类型的成员，只允许类本身和子类进行访问，但是不能使用 from module import* 语句导入
# __for 以双下划线开头的表示private类型的成员，只允许本身进行访问




