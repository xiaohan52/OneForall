# 文件的备份
def copyFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名称：')
    file_list=old_file.split('.')
    # 构造新的文件名.加上备份的后缀
    new_file=file_list[0]+'_备份'+file_list[1]
    old_f=open(old_file,'r')   #  打开需要备份的文件
    new_f=open(new_file,'w')   #  写的模式去打开新文件，不存在则创建
    content=old_f.read()       #  将文件内容读取出来
    new_f.write(content)       #  将读取的文件写入到备份文件
    old_f.close()
    new_f.close()
    pass

copyFile()