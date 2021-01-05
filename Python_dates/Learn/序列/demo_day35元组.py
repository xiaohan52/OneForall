# 元组是一种不可变的序列，在创建之后不能做任何改动，使用（） 来创建，而且可以是任何类型
# 当元组中只有一个元素的时候，要加上逗号，不然解释器会当整型来处理
# 元组同样可以支持切片操作

tupleA = ()  # 空元组，没有意义
tupleA = ('abcd',89,2,9.12,'peter',[11,22,33])
print(tupleA)

# 元组的查询
for item in tupleA:
    print(item,end=' ')

print(tupleA[2])
print(tupleA[2:4])

print(tupleA[::-1])

print(tupleA)




