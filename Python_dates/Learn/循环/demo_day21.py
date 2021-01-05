# 单分支流程设计
# if 条件表达式:
# 代码指令
# ……
print('——————成绩录入系统——————')
score = int(input('请输入数据\n'))  #input输入的是字符串类型，不是数字类型，如果不类型转换会报错

if score < 60:  # 满足条件则会进入下面
    print('成绩为D等级，需要加油！')
    pass
elif score < 70:
    print('成绩为C等级，加油！')
    pass
elif score < 80:
    print('成绩为B等级，不错！')
    pass
elif score < 90:
    print('成绩为A等级，棒！')
    pass
else :
    print('成绩为S等级，为你骄傲！')
    pass

