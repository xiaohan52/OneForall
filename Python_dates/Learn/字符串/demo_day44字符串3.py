# 格式化字符串，意思就是可以弄个模板，留几个空位这样可以直接输入字符串
# 使用%操作符，也就是%s,d,c,x,f,r,E
template = '编号：%09d\t 公司名称:  %s\t 官网： http://www.%s.com'      # 定义模板
context1 = (7,'百度','baidu')
context2 = (8,'xph','iloveu')
print('——————格式化输出——————')
print(template%context1)
print(template%context2)

# 字符串对象的format()方法可以进行字符串格式化，语法格式为:str.format(args)
# 创造模板需要使用{} 和: 指定占位符，基本语法为: {[index][:[[fill]align][sign][#][width][.precision][type]]}
# S 对字符串类型格式化 D 十进制整数 C 将十进制转化为Unicode E 转换为科学计数法再格式化
template1 = '编号：{:0>9s}\t 公司名称:  {:s}\t 官网： http://www.{:s}.com'      # 定义模板
context1 = template1.format('7','百度','baidu')
context2 = template1.format('8','xph','iloveu')
print('——————格式化输入——————')
print(context1)
print(context2)