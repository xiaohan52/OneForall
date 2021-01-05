# 打印直角三角形
# row = 1
# while row <= 7:
#     j = 1
#     while j <= row:
#         print('*',end=' ')
#         j += 1
#         pass
#     print('')
#     row += 1

# 打印倒着的直角三角形
#    row = 7
#  while row >= 1:
#      j = 1
#      while j <= row:
#      print('*',end=' ')
#          j += 1
#          pass
#      print('')
#  row -= 1

# 等腰三角形的打印
row = 1
while row <= 10:
    j = 1
    while j <= 10-row:
        print(' ',end ='')
        j += 1
        pass
    k = 1
    while k <= 2*row - 1:   # 控制打印*号
        print('*',end ='')
        k += 1
        pass
    print('')
    row += 1