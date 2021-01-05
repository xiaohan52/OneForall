import re
# .的使用    匹配规则是除了换行符之外的字符
# [abc]匹配abc中的任意一个字符
# \d 匹配一个数字，0-9
# \D 匹配非数字
# \s 匹配空格 空白  space tab
# \S 匹配非空格
# \w 匹配单词和字符 a-z A-Z _ 0-9
# \W 匹配非单词和字符

str1 = 'hello'
res1 = re.match('[eh]',str1)
print(res1.group())
res2 = re.match('....',str1)
print(res2.group())
res3 = re.match('\D\D',str1)
print(res3.group())

# 匹配字符数量
# * 匹配前一个字符出现0次或无数次，即可有可无
# + 匹配前一个字符出现1次或无数次，即至少为1
# \? 匹配前一个字符出现1次或者0次，即要么出现1次要么不出现
# {m} 匹配前一个字符出现m次
# {m,} 匹配前一个字符至少出现m次
# {n,m} 匹配前一个字符出现从n到m次

res4=re.match('[a-z]*[A-Z]*','myyamnMMdadanMNFdasdMMH')
print(res4.group())
res5=re.match('[a-z]+','dwadasadadwadIMHAPPYdads')
print(res5.group())

# 贪婪模式和非贪婪模式
# python中正则表达式一般都是贪婪模式以求最大化的查找数据，但是可以在匹配类型后加上？
rs = re.match('\d{6,9}?','123456789')
print(rs.group())
rs1 = re.match('\d{6,9}','123456789')
print(rs1.group())