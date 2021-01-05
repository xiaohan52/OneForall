# 文件的操作
# 打开文件    open('文件名称','打开模式')         # 打开模式可以是文件不存在，也可以是创建一个这样的文件
#   打开模式：a:可以编写  r:只读    w:写入，创建新文件  r+:读写，文件指针放在开头 w+:读写，已经存在会覆盖
# 默认的编码是gdk，是中文编码，最好指定一个编码类型
# fobj = open('123.txt','w',encoding='UTF-8')
# # 开始操作
# fobj.write('在摸鱼的大海上')
# fobj.write('狂风卷积着咸鱼')
# fobj.close()

# 以二进制的形式去写数据  wb

fobj = open('123.txt','w')  # str -> bytes
fobj.write('在摸鱼的大海上\n')
fobj.write('狂风卷积着咸鱼\n')
fobj.write('在摸鱼和学习之间\n')
fobj.write('我选择了摸鱼\n')
fobj.write('摸鱼使我快乐\n')
fobj.close()

# print(fobj.read())   # 读取所有数据
# print(fobj.readline())  # 读取行

# with  上下文管理
# 不管在处理语句中是否发生异常，都能保证 with语句执行完毕后已经关闭打开的文件句柄
# 实例   def main()
#            with open('123.txt','w')  as  f
#            content = f.read()
#            print(content)
#       main()

# # 文件读取的几种情况
# read r r+ rb rb+
# r r+ 只读 适用于普通的读取场景
# rb rb+ 适用于读取文件，图片，视频，音频
# write w w+ wb wb+ a ab
# w wb+ w+ 每次都会去创建文件
# 二进制读写的时候要注意编码问题   默认的时候是GDK
# a ab a+ 在原有的文件上去追加  不会去每次覆盖文件
