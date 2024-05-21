import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import plotly.express as px
from pyecharts import options as opts
from pyecharts.charts import Liquid,Pie,Line,Bar,Sunburst,Gauge
from pyecharts.globals import ThemeType

data = pd.read_excel('yibiao.xlsx')
#创建仪表盘对象:创建了一个仪表盘（Gauge）对象，并将其赋值给变量gau。这个仪表盘对象之后会被用来配置和显示数据。
gau = Gauge()
#配置和显示仪表盘:series_name='平均感受': 设置系列名称为“平均感受”
# data_pair=[('物联网专业喜爱程度',65)]: 这里设置了一个数据对，表示“物联网专业喜爱程度”的值为65。
# min_=-30, max_=80: 设置仪表盘的最小值和最大值，分别为-30和80。split_number=8: 将仪表盘分成8个部分或区间。
# detail_label_opts=...: 配置仪表盘中心的详细信息标签。
# axisline_opts=...: 配置仪表盘的轴线。
# 其中，linestyle_opts=...配置了轴线的样式，包括颜色和宽度。颜色是一个列表，表示从起点到终点的颜色渐变，width=20表示轴线的宽度为20。
gau.add(series_name='平均感受',data_pair=[('物联网专业喜爱程度',65)],
        min_=-30,max_=80,
        split_number=8,
        detail_label_opts=opts.GaugeDetailOpts(formatter='{value} %',offset_center=['0%','80%']),
        axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(0.3,'#67e0e3'),(0.7, '#37a2da'), (1, '#fd666d')], width=20)))

gau.render('仪表盘.html')

