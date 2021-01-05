# 检索字符串，主要有以下几个方法

# count()方法用于检索指定字符串在另外一个字符串中出现的次数，语法格式为： str.count(sub[,start[,end]])
#                                                            原字符串  子字符串  可选参数(起始位置)   可选参数(结束位置)
str1 = '@Xph @Cwx @Pq'
print('字符串中包含',str1.count('@'),'个@符号')

# find()方法用于检索是否包含指定字符串，其语法格式为： str.find(sub[,start[,end]])
print('字符串中@符号首次出现的位置索引为',str1.find('@'))
print('字符串中@符号首次出现的位置索引为',str1.find('!'))    # 若输入的子字符串在原字符串中不存在，将返回-1

# index()方法和find()方法类似，也是用于检索是否包含指定的字符串，只不过如果不存在子字符串的时候，会抛出异常
print('字符串中@符号首次出现的位置索引为',str1.index('@'))
# print('字符串中@符号首次出现的位置索引为',str1.index('!'))

# startswith()方法用于检索字符串是否以指定子字符串开头，如果是就是ture，其语法结构为: str.startswitch(prefix[,start[,end]])
print('判断字符串是否以@开头：',str1.startswith('@'))
print('判断字符串是否以@开头：',str1.startswith('!'))

# endswith()方法，来检索字符串是否以指定子字符串结尾，同startswith(),其语法结构为：str.endswith(prefix[,start[,end]])
print('判断字符串是否以@结尾',str1.endswith('@'))
print('判断字符串是否以q结尾',str1.endswith('q'))

# python中字符串对象提供了lower() 和upper()方法进行字母的大小写转换，即str.lower()  str.upper()
print(str1.lower())            # 全部转化为小写字母
print(str1.upper())            # 全部转化为大写字母

# python 中可以去除字符串中空格以及特殊字符 strip() 语法格式为：str.strip([char]) char 可以指定要去除的字符，可以指定多点
st2 = 'http://www.ilovexph.com   \t\n\r'
print('原字符串：',st2)
print('去除特殊字符的字符串:',st2.strip())
st3 = '@www.@'
print('原字符串：',st3)
print('去除@.之后的字符串：',st3.strip('@.'))
# lstrip() rstrip()方法可以去除左边，右边的空格和特殊字符

