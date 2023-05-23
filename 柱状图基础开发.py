"""
演示基础柱状图的开发
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
# 使用Bar构建基础柱状图
bar = Bar()
# 添加x轴的数据
bar.add_xaxis(["中国","美国","日本","德国","韩国","加拿大","法国"])
# 添加y轴的数据
bar.add_yaxis("GDP",[5,30,20,40,30,28,30],label_opts=LabelOpts(position="right"))
# 反转x轴和y轴
bar.reversal_axis()
# 绘图
bar.render("基础柱状图.html")
