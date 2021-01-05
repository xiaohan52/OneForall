import re
# 1.将下列文段中的s替换为S输出

data = 'Save your heart for someone who cares'
res=re.sub('s','S',data)
print(res)

data1='<span>三生三世，十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>'
res1=re.compile(r'<span>(.*)</span><span>(.*)</span><span>(.*)</span>')
result=res1.findall(data1)
print(result)