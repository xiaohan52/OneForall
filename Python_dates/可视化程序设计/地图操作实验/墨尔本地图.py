import csv
import time
import folium
import webbrowser
from folium.plugins import MarkerCluster

# 创建游标对象对墨尔本地图进行接受   [坐标，初始缩放级别，地图类型]
m = folium.Map(location=[-37.8263,144.9595],zoom_start=12, tiles='OpenStreetMap')
#  点击获取经纬度
m.add_child(folium.LatLngPopup())
# 添加一个标记对象
marker_cluster = MarkerCluster().add_to(m)

# folium.Marker(
#     location=[-34.50,144.58],
#     popup='Town_Hall-West',
#     # icon=folium.Icon(icon='cloud')          # 设置图标，可以不设置
# ).add_to(m)

# 获取数据
csv_data1 = csv.reader(open(r'C:\Users\MACHENIKE\Desktop\KSHCX\墨尔本人行道监控数据\2012_01-HOUR.CSV','r'))
data=[]
for line in csv_data1:
    data.append(line)
    pass
# if __name__ == "__main__":
#     n=7
# # 计时开始
# for n in range(0,20):
#     t0 = time.time()
#     address=data[0][n]
#     n+=1
#     t1 = time.time()
#     total = t1 - t0
#     print("消耗时间：{}".format(total))

x=0
for y in range(0,20):
    time.sleep(5)
    for x in range(0,288):
        m.add_child(marker_cluster)
        x+=1
        y = 7
        number=data[x][y]
        # time.sleep(1)
        folium.Marker(
            location=[-37.8200, 144.9324],
            icon=None,
            popup=number,
        ).add_to(marker_cluster)
        # 将对象添加到地图中
        m.add_child(marker_cluster)
        pass
    y+=1
    pass

# 将对象添加到地图中
m.add_child(marker_cluster)
#  点击放置标记
# m.add_child(folium.ClickForMarker(popup='Waypoint'))
m.save("墨尔本人行道监控.html")
webbrowser.open("墨尔本人行道监控.html")

