# 文件的备份
def copyBigFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名称：')
    file_list=old_file.split('.')
    # 构造新的文件名.加上备份的后缀
    new_file=file_list[0]+'_备份'+file_list[1]
    try:
        # 监视要处理的逻辑
        with open(old_file,'r') as old_f,open(new_file,'w') as new_f:
            while True:
                conent = old_f.read(1024)   # 一次性读取1024字符
                new_f.write(conent)
                if len(conent)<1024:
                    break
    except Exception as msg:
        print(msg)
    pass

copyBigFile()