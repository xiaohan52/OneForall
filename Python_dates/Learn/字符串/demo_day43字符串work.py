# 假设以及注册的会员名称保存在一个字符串中，以'|'进行分隔
username_1 = '|MingRi|mr|mingrisoft|WGH|MRSoft'
username_2 = username_1.lower()
regname_1 = input('请输入要注册的会员名：\n')
regname_2 = '|' + regname_1.lower() + '|'
if regname_2 in username_2:
    print('会员名:',regname_1,'已经存在')
else:
    print('会员名',regname_1,'可以注册')