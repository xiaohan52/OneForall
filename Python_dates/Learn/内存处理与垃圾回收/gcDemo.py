import sys
import psutil
import os
import gc
def showMemSize(tag):
    pid=os.getpid()
    p=psutil.Process(pid)
    info=p.memory_full_info()
    memory=info.uss/1024/1024
    print('{} memory used: {} MB'.format(tag,memory))
    pass

# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a=[i for i in range(100000)]
    b=[i for i in range(100000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象a,b后')
    print(sys.getrefcount(a))                             # 引用计数
    print(sys.getrefcount(b))
    # del a
    # del b
    pass
func()
gc.collect()       # 手动释放                              # 信息标记分代收集
showMemSize('完成之后')


# sys.getrefcount()    # 对于操作的次数进行一个计数
# 好处1.简单2.具有实时性，一旦没有引用便可以直接释放内存，处理回收内存的时间分摊到了平时
# 缺点1.维护引用消耗了资源2.循环引用，导致内存泄漏

# a=[]
# print(sys.getrefcount(a))

#
