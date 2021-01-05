# 通过python中的re模块学习正则表达式
import re

# re.Match方法       re.Match(pattern,string,flags=0)
# 仅仅是尝试从字符串的起始位置[第一个字符]匹配一个规则
data='Python is the best language in the world'
res1=re.match('P',data)       # 精确匹配第一个字母(字符)
res2=re.match('Python',data)  # 精确匹配第一个单词(字符)
res3=re.match('y',data)       # 无法匹配非第一个字符
# print(type(res1),type(res2))             # 返回<class 're.Match'>
# print(res1.group(),res2.group())           # 取值成功会返回到group

# 如果同时使用多个标志位使用|分割，比如re.I,re.M
# flags可选标识符
# re.I 对大小写不敏感
# re.L 做本地化识别(locale-aware)匹配
# re.M 多行匹配，影响^和$
# re.S 使.匹配包括换行在内的所有字符
res=re.match('python',data,re.I|re.M)         # 表示忽略大小写对字符进行查找
if res:
    print('匹配成功')
    print(res)
    print(res.group())                   # 输出需要查找的字符
else:
    print(res)
    print('匹配失败')
  # print(res.group())                   # 如果匹配失败是没有group()对象，因为是一个空对象

# 可以使用group(num)或groups()匹配对象函数来获取函数匹配式
# group(num)可以获取匹配到的数据 如果有多个匹配结果的话 那么会以元组的形式 存放到group对象中，可以通过下标去获取
# groups()和group(num)一样，只不过数据是以元组类型去取和显示

res5=re.match('(.*) is (.*?) .*',data,re.I)
print(res5.group(1))
print(res5.group(2))
print(res5.groups())

