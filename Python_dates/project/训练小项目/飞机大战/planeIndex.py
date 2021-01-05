import pygame       # 引用第三方模块
import random
import time
from pygame.locals import *
'''
1.创建玩家飞机类
'''
class xphplane(object):
    def __init__(self,sceen):
        '''
        初始化函数
        :param sceen:主窗体对象
        '''
        # 飞机的默认位置
        self.x=260
        self.y=480
        # 设置要显示内容的窗口
        self.screen=sceen
        # 生成飞机的图片对象
        self.imageName='飞机.jpg'
        self.image=pygame.image.load(self.imageName)
        # 用来存放子弹的列表
        self.bulletList=[]
        pass
    def moveleft(self):
        '''
        向左移动
        :return:
        '''
        if self.x>0:
            self.x-=15
        pass
    def moveright(self):
        '''
        向右移动
        :return:
        '''
        if self.x<560:
            self.x+=15
        pass
    def moveup(self):
        '''
        向上移动
        :return:
        '''
        if self.y>0:
            self.y-=15
        pass
    def movedown(self):
        '''
        向下移动
        :return:
        '''
        if self.y<540:
            self.y+=15
        pass
    def display(self):
        '''
        在主窗口中显示飞机
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        needDelItemList=[]
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历需要删除的子弹列表
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()     # 让子弹开始移动
        pass


    # 发射子弹
    def shoot(self):
        # 创建一个子弹对象
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
        pass

    pass
'''
2.创建子弹类
'''
class Bullet(object):
    def __init__(self,x,y,screen):
        '''

        :param x:
        :param y:
        :param screen:
        '''
        self.x=x+27
        self.y=y-5
        self.screen=screen
        self.image=pygame.image.load('Bullet.jpg')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=0.1
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y<0:
            return True
        else:
            return False
        pass
    pass
'''
3.创建敌机类
'''
class Enemyplane:
    def __init__(self,screen):
        # 默认的设置一个方向
        self.direction='right'
        # 飞机的默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        self.bulletList=[]
        # 生成飞机的图片对象
        self.imageName = '敌机.jpg'
        self.image = pygame.image.load(self.imageName)
        pass
    def display(self):
        '''
        显示敌机以及子弹位置的信息
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历需要删除的子弹列表
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让子弹开始移动
        pass
        pass
    def shoot(self):
        '''
        敌机随机的进行发射
        :return:
        '''
        num=random.randint(1,500)
        if num==3:
            newBullet=EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        '''
        敌机随机进行移动
        :return:
        '''
        if self.direction=='right':
            self.x+=0.3
            pass
        elif self.direction=='left':
            self.x-=0.3
            pass
        if self.x>580-10:
            self.direction='left'
            pass
        elif self.x<0:
            self.direction='right'
    pass
'''
创建敌机的子弹类
'''
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y+10
        self.screen=screen
        self.image=pygame.image.load('Bullet1.jpg')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y+=0.05
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y>580:
            return True
        else:
            return False
        pass
    pass
def key_control(xphobj):
    '''
    定义普通的函数，用来实现键盘的检测
    :param xphplane:可控制的对象
    :return:
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('左')
                xphobj.moveleft()   # 调用函数进行左移动
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('右')
                xphobj.moveright()   # 调用函数进行右移动
                pass
            elif event.type == K_w or event.key == K_UP:
                print('上')
                xphobj.moveup()   # 调用函数进行上移动
                pass
            elif event.type == K_s or event.key == K_DOWN:
                print('下')
                xphobj.movedown()   # 调用函数进行下移动
                pass
            elif event.type == K_SPACE or event.key == K_SPACE:
                print('开火')
                xphobj.shoot()
                pass
            pass
    pass
def main():
    # 首先创建一个窗口对象，用来承载目标
    screen=pygame.display.set_mode((580,580),depth=32)
    # 设定一个背景图片
    background=pygame.image.load('背景.jpg')
    # 设置一个title
    pygame.display.set_caption('飞机大战！')
    # 设定背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) # -1表示为无限循环

    # 创建一个飞机对象
    xph = xphplane(screen)
    # 创建一个敌机对象
    enemyplane = Enemyplane(screen)

    # 设定需要显示的内容
    while True:
        screen.blit(background,(0,0))
        # 显示玩家飞机的图片
        xph.display()
        # 显示敌人飞机的照片
        enemyplane.display()
        # 敌机随机移动
        enemyplane.move()
        # 敌机随机发射
        enemyplane.shoot()
        # 获取键盘事件
        key_control(xph)
        # 每时每刻都需要更新显示的内容
        pygame.display.update()
        pass
if __name__=='__main__':
    main()
