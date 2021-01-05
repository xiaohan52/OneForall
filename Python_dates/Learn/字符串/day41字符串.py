# 字符串编码即为ASCII码,而且在python中有两种字符串类型，分别为str和bytes，一个是Unicode码还有一个是二进制，不能一起拼接使用
# str在内存中一般需要以Unicode表示，但是如果在网络上或者是磁盘上，需要使用bytes类型
# str和bytes之间可以使用encode()和decode() 方法来进行转换，而且互逆

# encode()方法为str对象的方法，用于将字符串转换为二进制数据，语法格式如下： str.encode([encoding="utf-8"][,errors="strict"])
verse = '野渡无人舟自横'
byte = verse.encode('GBK')                           # 采用GBK编码来转换为二进制数据
byte1 = verse.encode('UTF-8')                        # 采用UTF-8编码来转换为二进制数据
print('原字符串：',verse)                              # 输出原字符串
print('转换GBK后:',byte)                                 # 输出转换GBK后的二进制数据
print('转换UTF-8后:',byte1)                              # 输出转换UTF-8后的二进制数据

# 使用decode()方法解码   decode()方法为bytes对象的方法，用于将二进制转化为字符串，也称解码
# 其语法格式如下: bytes.decode([encoding="utf=8"][,errors="strict"])
print('解码后:',byte.decode("GBK"))    # 对二进制数据进行解码

# 可以使用+来进行字符串的拼接
mot_en = '相知即是相遇,'
mot_cn = '记忆便是相遇'
print(mot_en + mot_cn)

# 字符串不允许直接和其他类型的数据拼接，但是可以通过类型转换来同类型之后拼接
str1 = '今天我一共走了'     # 定义字符串
num = 12090              # 定义一个整数
str2 = '步'               # 定义字符串
print(str1 + str(num) + str2)

# 计算字符串的长度，可以使用len() 函数来计算字符串的长度： len(string)
length = len(str1)
print(length)
length1 = len(str1.encode())            # 计算GBK编码的字符串的长度
print(length1)

# 截取字符串，可以使用切片方法 string[start:end:step]
strr = '人生苦短，我用python'            # 定义字符串
substrr1 = strr[1]                     # 截取第二个字符
substrr2 = strr[5:]                    # 从第六个字符开始截取
substrr3 = strr[:5]                    # 从左边开始截取第五个字符
substrr4 = strr[2:5]                   # 截取第三个到第五个字符
print('原字符串：',strr)
print(substrr1 + '\n' + substrr2 + '\n' + substrr3 + '\n' + substrr4)

# 分割，合并字符串，字符串对象的split()方法可以实现字符串的分割操作，语法格式如下:str.split(sep.maxsplit)
# 在split()方法中，如果布指定sep参数，那么也不能指定maxsplit参数
str5 = '陈 文 星 爱 谢 佩 涵  >>>   www.loveU1314.com'
print('原字符串',str5)
list1 = str5.split()             # 采用默认分隔符来进行分割
list2 = str5.split('>>>')        # 采用多个字符来进行分割
list3 = str5.split('.')          # 采用.来进行分割
list4 = str5.split(' ',4)         # 采用 来进行分割，而且只分割前4个
list5 = str5.split('>')          # 采用>来进行分割
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

str6 = '@谢佩涵 @陈文星 @佩奇'
list6=str6.split(' ')         # 用空格分割字符串
print('您@的好友有:')
for item in list6:
    print(item[1:])

# 合并字符串，使用字符串对象的join()方法实现，其语法格式为： strnew = string.join(iterable)
list_friend = ['谢佩涵','陈文星','佩奇']        # 好友列表
str_friend = '@'.join(list_friend)           # 用空格加上@符号进行连接
at = '@' + str_friend                    # 由于使用join()方法时，第一个元素前不加分隔符，所以需要再前面加上@符号
print('您要@的好友：',at)