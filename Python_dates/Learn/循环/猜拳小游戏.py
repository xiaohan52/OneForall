# 多分枝的演练
# 猜拳小游戏
# 0:石头 1:剪刀 2:布
import random  #导入可以产生随机数的模块
# 计算机，人
Y = 0
S = 0
P = 0
index = 1
n = int(input('小宝宝想玩几次猜拳呀：\n'))

while index <= n:

    person = int(input('请出拳：【0:石头 1:剪刀 2:布】\n'))
    if person == 0:
        print('你出的是石头')
    elif person == 1:
        print('你出的是剪刀')
    elif person == 2:
        print('你出的是布')
    else:print('你出错了啦，请输入0，1，2')

    computer = random.randint(0,2)   #电脑产生随机数
    if  computer == 0:
        print('电脑出的是石头')
    elif computer ==1:
        print('电脑出的是剪刀')
    else:
        print('电脑出的是布')
    if person == 0 and computer == 1 or person == 1 and computer == 2 or person == 2 and computer ==0:
        print('厉害了，你赢了！')
        Y = Y+1
    elif person ==0 and computer == 0 or person == 1 and computer == 1 or person == 2 and computer == 2 :
        print('平局，下一把！')
        P = P+1
    else:
        S = S+1
        print('你输了，再试一次吧！')
        pass
    index += 1




print('一共%s局猜拳，你赢了电脑%s局，你输了电脑%s局，你俩平局%s次'%(n,Y,S,P))
if Y == n:
    print('你就是天纵之才！今天的好运都被你占去了！快去找星宝宝炫耀吧~~~')
elif Y > S :
    print('你已经赢了电脑%s局辣！今天也是幸运的你呢~~~'%(Y))
elif Y == S:
    print('今天的运气正常哦~享受今天的好天气吧~~~')
else:
    print('运气差到爆了辣！！！！快找星宝宝去诉苦吧~')
