a=100
b=100
print(id(a))
print(id(b))
del a
del b
c=100
print(id(c))
# 大整数池和小整数池的区别
# 1.大整数池是没有提前的创建好对象，是个空池，需要自己创建，创建后会把整数对象保存到其中，以后都不需要创建，直接使用
# 2.小整数池是提前将[-5,256]的数据都提前创建好
