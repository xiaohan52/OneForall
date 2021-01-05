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

data=[10000,10000]

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
for x in range(0,3232):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8200, 144.9324],
        icon=None,
        popup=1,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,283):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[ -37.8101, 144.9913],
        icon=None,
        popup=2,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,524):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8177, 144.9902],
        icon=None,
        popup=3,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,878):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8256, 144.9568],
        icon=None,
        popup=4,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,773):
    m.add_child(marker_cluster)
    x+=1

    # time.sleep(1)
    folium.Marker(
        location=[-37.8255, 144.9707],
        icon=None,
        popup=5,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,2763):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8255, 144.9571],
        icon=None,
        popup=6,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,105):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8227, 144.9476],
        icon=None,
        popup=7,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,1616):
    m.add_child(marker_cluster)
    x+=1

    # time.sleep(1)
    folium.Marker(
        location=[-37.8211, 144.9691],
        icon=None,
        popup=8,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,261):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[ -37.8054, 144.9480],
        icon=None,
        popup=9,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass
for x in range(0,246):
    m.add_child(marker_cluster)
    x+=1
    # time.sleep(1)
    folium.Marker(
        location=[-37.8070, 144.9629],
        icon=None,
        popup=10,
    ).add_to(marker_cluster)
    # 将对象添加到地图中
    m.add_child(marker_cluster)
    pass


# 将对象添加到地图中
m.add_child(marker_cluster)
#  点击放置标记
# m.add_child(folium.ClickForMarker(popup='Waypoint'))
m.save("墨尔本人行道监控.html")
webbrowser.open("墨尔本人行道监控.html")

