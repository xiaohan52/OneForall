from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 用于测试的例子，部分取自 Faker ，也就是 from pyecharts.faker import Faker
provinces = ["广东", "北京", "上海", "辽宁", "湖南", "四川", "西藏"]
guangdong_city = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市"]
country = ["China", "Canada", "Brazil", "Russia", "United States", "Africa", "Germany"]
value = [300, 100, 2000, 800, 10000, 400, 5000]

# 显示其中的某些省市和数据
def map_base() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(provinces, value)], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="map-基本图形"))
    )
    return c
if __name__ == '__main__':
    city_map = map_base()
    city_map.render(path="test_map_1.html")


    # 连续性数据显示，不同颜色不同省份
    def map_visualmap() -> Map:
        c = (
            Map()
                .add("", [list(z) for z in zip(provinces, value)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="连续型数据"),
                visualmap_opts=opts.VisualMapOpts(max_=2000),
            )
        )
        return c


    if __name__ == '__main__':
        city_ = map_visualmap()
        city_.render(path="test_map_1.html")


