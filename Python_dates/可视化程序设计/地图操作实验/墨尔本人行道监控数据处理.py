import csv
csv_data1 = csv.reader(open(r'C:\Users\MACHENIKE\Desktop\KSHCX\墨尔本人行道监控数据\2012_01-HOUR.CSV','r'))
# 将数据都存储在data中
data=[]
for line in csv_data1:
    data.append(line)
    pass

x=0

for x in range(0,288):
    x+=1
    y=7
    number=data[x][y]
    print(number)
    pass


