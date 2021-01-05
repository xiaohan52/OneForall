# 猜年龄小游戏，有以下三点要求
# 1.允许用户最多猜3次
# 2.每尝试3次之后，如果还没猜对，就询问是否还想继续玩，回答Y or N
# 3.如果猜对了就直接退出
import random
times = 0
count = 8
n = int(random.randint(0,50))
while times <= 8:
    age = int(input('请输入您要猜的年龄\n'))
    if age == n:
        print('恭喜您，猜对了')
        pass
    elif age > n:
        print('猜大了，再试试')
        pass
    else:
        print('猜小了，再试试')
        pass
    times += 1

    if times == 8:
        choose = input('还想不想继续猜呢？Y/N\n')
        if choose == 'Y' or choose == 'y':
            times = 0
            pass
        elif choose == 'N' or choose == 'n':
            print('谢谢游戏！')
            break
        else:
            print('请输入您的选择')
            choose = input('Y/N\n')
    pass