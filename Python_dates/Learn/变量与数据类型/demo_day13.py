# 逻辑运算符 and or not

# and 判断条件 只有两边都为ture，才会返回ture
# 定义4个变量
print('——————and——————')
a,b,c,d = 23,18,10,3
print(a+b>c and c<d)
print(a>b and c>d)

# or 条件有一个为ture则结果为ture
print('——————or——————')
print(a<b or c>d)
print(a+d>c+b or a-b<c-d)

# not 取反，真假切换
print('——————not——————')
print(not a<b)
print(not a>b)

# 优先级 ()  ->  not  -> and  ->or
print('————优先级测试————')
print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and 3<2)

# 赋值运算符
# += -= *= /=

print('————赋值运算符测试————')
a+=c
b*=c
print(a)
print(b)