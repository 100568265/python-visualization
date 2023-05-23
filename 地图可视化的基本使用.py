"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
myMap = Map()
# 准备数据
data = [
    ("黑龙江省", 99),
    ("青海省", 199),
    ("湖南省", 299),
    ("广东省", 40000),
    ("四川省", 499)
]
# 添加数据
myMap.add("测试地图", data, "china")

# 设置全局选项
myMap.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 100, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 5000, "max": 9999, "label": "100-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"}
        ]

    )
)
# 绘图
myMap.render()
# 设置全局选项
