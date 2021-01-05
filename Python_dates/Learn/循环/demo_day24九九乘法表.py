# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d*%d=%d" %(row,col,row*col),end='')
        col += 1
        pass
    print()
    row += 1
    pass

#  倒三角的九九乘法表
#    row = 9
# while row >= 1:
#        col = 1
#      while col <= row:
#          print("%d*%d=%d" %(row,col,row*col),end='')
#         col += 1
#        pass
#     print()
#    row -= 1
# pass