# if-else 的嵌套使用
# 一个场景需要多种选择，而且需要执行内部条件，层层递进
credit = int(input('请输入您的学分\n'))
grade = int(input('请输入您的成绩\n'))
if credit >= 10:
    if grade >= 80:
        print('恭喜您！您可以升学！')
        pass
    else:
        print('很遗憾，您的成绩没有达到要求')
        pass
    pass
else:
    print('很遗憾，您没有达到要求')