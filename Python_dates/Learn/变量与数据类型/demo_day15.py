# python使用input来接受键盘输入的数据，而且都是str()类型的，需要转化为int
name = input('请输入你的名字\n')
# 如果是用格式化输入，在输入时必须注意，input都是str类型，需要强制类型转换
# 强制类型转换方式为： 直接在前面加上int，之后括号括起来，如int(input(''))
age = int(input('请输入你的年龄\n'))
addr = input('请输入你的地址\n')
qq = input('请输入你的qq\n')
phone = input('请输入你的电话\n')
print('我的名字是%s,我今年%d岁,我来自%s,我的qq是%s,我的电话是%s,这是我的个人信息' %(name,age,addr,qq,phone))