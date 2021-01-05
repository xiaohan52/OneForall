# 决战紫禁之巅，顾名思义有两个人物决战，分别为陈文星和谢佩涵，其中含有血量以及姓名，攻击方式以及其他可添加的东西
#
# 含有属性：血量，姓名
# 含有方法：捅一刀10滴血tong(),砍一刀15滴血kan(),回复血量10滴huixue()
# __str__打印玩家状态

# 第一步 需要先定义一个l类[角色]
import time   # 导入时间库
class Role:
    def __init__(self,name,hp):
        '''
        构造初始化函数
        :param name:角色姓名
        :param hp:角色血量
        '''
        self.name = name
        self.hp = hp
        pass
    def tong(self,enemy):
        '''
        捅一刀，掉10血
        :param enemy: 对方的血量
        :return:
        '''
        enemy.hp-=10
        info='[%s]捅了[%s]一刀'%(self.name,enemy.name)
        print(info)
        pass
    def kan(self,enemy):
        '''
        砍一刀，掉15血
        :param enemy:对方的血量
        :return:
        '''
        enemy.hp-=15
        info = '[%s]砍了[%s]一刀' %(self.name, enemy.name)
        print(info)
        pass
    def hui(self):
        '''
        回复血量10滴
        :return:
        '''
        self.hp+=10
        info='[%s]喝了果粒橙，增加10滴血'%(self.name)
        print(info)
        pass
    def __str__(self):
        return '%s还剩下%s的血量'%(self.name,self.hp)
# 创建两个实例化对象
name1 = str(input('请输入玩家1的姓名：\n'))
name2 = str(input('请输入玩家2的姓名：\n'))
hp = 100
player1 = Role(name1,hp)
player2 = Role(name2,hp)
number = int(input('请输入想要游戏的回合数'))  # 输入需要游戏的回合数
i=1
i1=1
number1=number+1
for i1 in range(number1):        # 一共number1个回合，每回合每个角色只能进行一个活动
            i1+=1
# 请玩家一进行回合操作
            if player2.hp<=0:
                print('恭喜%s获得战斗的胜利' % player1.name)
                break
            else:
                action=int(input('请%s选择要做的事情[1.捅一刀 2.砍一刀 3.回血]'%player1.name))
                if action==1:
                    player1.tong(player2)  # 玩家一捅了玩家二一刀
                    print(player1)
                    print(player2)
                    print('*********************')
                    pass
                elif action==2:
                    player1.kan(player2)  # 玩家一砍了玩家二一刀
                    print(player1)
                    print(player2)
                    print('*********************')
                    pass
                elif action==3:
                    player1.hui()
                    print(player1)
                    print(player2)
                    pass
                time.sleep(1)   # 暂停休眠一秒钟方便看结果
                pass
# 请玩家二进行回合操作
            if player1.hp <= 0:
                    print('恭喜%s获得战斗的胜利' % player2.name)
                    break
            else:
                action = int(input('请%s选择要做的事情[1.捅一刀 2.砍一刀 3.回血]' % player2.name))
                if action==1:
                    player2.tong(player1)  # 玩家二捅了玩家一一刀
                    print(player1)
                    print(player2)
                    print('*********************')
                    pass
                elif action==2:
                    player2.kan(player1)  # 玩家二捅了玩家一一刀
                    print(player1)
                    print(player2)
                    print('*********************')
                elif action==3:
                    player2.hui()
                    print(player1)
                    print(player2)
                    print('*********************')
                    pass
                time.sleep(1)  # 暂停休眠一秒钟方便看结果
pass
print('*****游戏结束*****')




