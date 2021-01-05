import argparse

# 创建一个解析器对象   以下语法是固定语法
parse=argparse.ArgumentParser(prog='系统登陆',usage='%(prog)s [options] usage',
                              description='系统自定义命令行的文件',epilog='my - epilog')

# 添加位置参数[必选参数]
parse.add_argument('LoginType',type=str,help='登陆系统类型')

# 添加而可选参数
parse.add_argument('-u',dest='user',type=str,help='你的用户名')
parse.add_argument('-p',dest='password',type=str,help='你的密码')


result = parse.parse_args()   # 开始解析参数

if(result.user=='root' and result.password=='123456'):
    print('Login success!')
else:
    print('Login fail!')