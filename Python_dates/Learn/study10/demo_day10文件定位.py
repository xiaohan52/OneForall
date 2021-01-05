# tell 返回指针当前所在位置
# with open('123.txt','r') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())
#

# truncate      可以对源文件进行截取操作
fobjB=open('123.txt','r')
print(fobjB.read())
fobjB.close()
print('截取之后的数据....')

fobjA=open('123.txt','r+')
fobjA.truncate(15)          # 保留前15个字符
print(fobjA.read())
fobjA.close()

# seek可以控制光标所在的位置

with open('123_备份txt','rb') as f:
    data = f.read(2)
    print(data.decode('gbk'))
    f.seek(-2,1)   # 相当于光标又设置到了0的位置
    print(f.read(4).decode('gbk'))