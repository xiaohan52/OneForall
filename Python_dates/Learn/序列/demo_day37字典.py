# 字典相当于Java中的map对象
# 字典通过键而不是索引来读取，字典是任意对象的无序集合，字典是可变的，而且可以使用任意嵌套，键必须唯一，而且不可变

# 字典的定义:   dictionary = {'key1':'value1','key2':'value2',......,'keyn':'valuen'}
dictionary = {'qq':'452138046','phone':'18772245428'}
print(dictionary)

# 1.通过映射函数创建字典   语法如下：dictionary = dict(zip(list1,list2))
# 根据名字和星座创建一个字典
name = ['绮梦','冷伊','香凝','黛兰']        # 作为键的列表
sign = ['水瓶座','射手座','双鱼座','双子座'] # 作为值的列表
dictionary = dict(zip(name,sign))        # 转换为字典
print(dictionary)
dictionary["碧落"] = "巨蟹座"           # 添加键值对，可以直接使用dictionary[key] = value  若元素已经存在，则自动变为修改此元素
print(dictionary)

# 2.通过给定的'键-值对'创造字典   语法如下: dictionary = dict(key1 = value1,key2 = value2,......,keyn = valuen)
# 还可以是用dict对象的fromkeys()方法创建值为空的字典，语法如下  dictionary = dict.fromkeys(list1)
name_list = ['齐萌','小依','湘宁','莫伊']     # 作为键的列表
dictionary1 = dict.fromkeys(name_list)
print(dictionary1)

# name1 = ['绮梦','冷伊','香凝','黛兰']
# sign1 = ['水瓶座','射手座','双鱼座','双子座']
# dict1 = {name1:sign1}      # 创建字典
# print(dict1)

# 可以通过   dictionary.clear()  来清除字典内的全部元素
# 而且可以通过 ger()方法来获取指定键的值 语法格式： dictionary.get(key[,default])
print("绮梦的星座为:",dictionary.get('绮梦'))

# 遍历字典可以通过字典对象的 item()方法，其语法格式为： dictionary.item()
for item in dictionary.items():
    print(item)
# 在python中，字典对象还提供了values() 和 keys()方法，用于返回字典的'值'和'键'
# 同时，可以直接使用del dictionary来进行字典的删除操作，同时也可以直接使用 del dictionary['key'] 的方法来进行单个元素的删除

# 字典推导式
import random
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print(randomdict)

