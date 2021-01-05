# 使用格式化输出来练习输出自己的个人信息
name = '陈文星'
age = '20'
qq = '452138046'
phone = '18086104516'
addr = '武汉轻工'
print('——————使用格式化输出个人信息——————')
print('我的名字是%s,我今年%s岁,我来自%s,我的qq是%s,我的电话是%s,这是我的个人信息' %(name,age,addr,qq,phone))
print('\n——————使用format来输出——————')
print('我的名字是{},我今年{}岁,我来自{},我的qq是{},我的电话是{},这是我的个人信息'.format(name,age,addr,qq,phone))

# 使用.format可以无视格式化输出的数据类型影响