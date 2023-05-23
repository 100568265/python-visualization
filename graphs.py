"""
演示pyecharts的基础入门
"""

#导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#得到折线图对象
line = Line()
#添加x轴数据
line.add_xaxis(["中国","美国","日本","德国","韩国","加拿大","法国"])
#添加y轴数据
line.add_yaxis("GDP",[5,30,20,40,30,28,30])

#设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

#生成图表
line.render()