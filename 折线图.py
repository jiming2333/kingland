import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import plotly.express as px
from pyecharts import options as opts
from pyecharts.charts import Liquid,Pie,Line,Bar,Sunburst
from pyecharts.globals import ThemeType
# 创建折线图对象
data = pd.read_excel('people.xlsx')
#这里使用Pyecharts库中的Line类来初始化一个折线图，并设置了主题为'MACARONS'。
line_chart_co = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        #添加X轴数据：
    .add_xaxis(list(data.index+1))
        # 添加y轴数据：
    .add_yaxis("物联网就业人数", data['物联网就业人数'], symbol='circle', label_opts=opts.LabelOpts(is_show=False))
    #设置全局选项：设置了折线图的标题、X轴和Y轴的选项以及图例的位置
    .set_global_opts(
        title_opts=opts.TitleOpts(title="物联网就业人数增长折线图",pos_left='center'),
        xaxis_opts=opts.AxisOpts(name="日期"),
        yaxis_opts=opts.AxisOpts(name="人数", min_=0, max_=1.0),
        legend_opts=opts.LegendOpts(pos_top='top', pos_left='right')
    )
)
print(data.index)
line_chart_co.render('折线图.html')


