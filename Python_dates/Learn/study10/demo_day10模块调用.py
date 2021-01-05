# # 如果是使用了import的话必须加上模块的名字
# import moudelTest
# res = moudelTest.add(2,7)
# print(res)
# print(moudelTest.diff(7,4))

# 如果是使用了from xxx import * 的话就不需要加上模块的前缀
from moudleTest.moudelTest import *
print(add(2,8))

print(diff(35,8))

# print(printInfo())    # 因为模块中使用了__all__魔术变量，导致无法使用模块中的printInfo方法

