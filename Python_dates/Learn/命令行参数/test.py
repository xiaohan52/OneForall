import sys
import argparse

# 创建一个解析器对象
parse=argparse.ArgumentParser(prog='my - 我自己的程序',usage='%(prog)s [options] usage',
                              description='my - 编写自定义命令行的文件',epilog='my - epilog')

# 添加位置参数[必选参数]
parse.add_argument('name',type=str,help='陈文星')
parse.add_argument('age',type=str,help='你的年龄')

# 添加而可选参数
parse.add_argument('-s','--sex',action='append',type=str,help='你的性别')
# 限定其范围
parse.add_argument('-s','--sex',default='男',choices=['男','male','女','female'],type=str,help='你的性别')
'''
可以通过add_argument 中各个行为来添加其表示 比如 action 来设计其行为 
metaver:帮助信息中显示的参数名称    
const:保存一个常量
defult:默认值
type:参数类型
choices:设置参数值的范围，如果其中的类型不是str 请指定为str
required:该选项是否为必选，默认为True
dest:参数名
'''

# print(parse.print_help())

resule = parse.parse_args()   # 开始解析参数
print(resule)
