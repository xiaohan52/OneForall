# 请设计一个程序，根据BMI的计算公式来求出BMI的值来判断是否健康
name = input('请输入您的姓名:\n')
height = float(input('请输入您的身高:\n'))
weight = float(input('请输入您的体重:\n'))
BMI = weight/(height**2)

if BMI < 18.5:
    print(name + '同学呀，你的体重BMI为%s，⑧太行呐，要长肉肉喽'%BMI)
    pass
elif 18.5 <= BMI <= 25:
    print(name + '同学呀，你的体重BMI为%s，是正常的哦'%BMI)
    pass
elif 25 <= BMI <=28:
    print(name + '同学呀，你的体重BMI为%s，有点超重了嗷，要多多运动哦~~'%BMI)
    pass
else:
    print(name + '同学呀，你的体重BMI为%s，需要多多运动哦，不然很容易生病呐~'%BMI)
    pass

