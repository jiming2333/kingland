import pandas as pd
from pyecharts.charts import Pie,Bar,Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType

#读取Excel数据:
sale=pd.read_excel('lunbo.xlsx',index_col=0)
#定义Timeline对象:初始化一个Timeline对象，用于后续的图表轮播
timeline=Timeline()
#定义函数c_charts:这个函数接受一个月份（month）作为参数，并返回一个重叠的柱状图和饼图。
# 使用`bar.add_xaxis`添加X轴的数据，即sale DataFrame的列名。
# 使用`bar.add_yaxis`添加柱状图的数据，这里从sale DataFrame中选取对应月份的数据。
# 创建一个饼图`pie`，其中饼图的标签是sale DataFrame的列名，数据是对应月份的数据。
# 使用`bar.overlap(pie)`将饼图叠加在柱状图上。
def c_charts(month):
    bar=Bar()
    bar.add_xaxis(list(sale.columns))
    bar.add_yaxis('不同地区一年就业人数',list(sale.loc[month]),bar_width='30px')
    pie=Pie()
    pie.add('就业占比',list(zip(sale.columns,list(sale.loc[month]))),
    radius=['15%','30%'],
    center=['80%','25%'])
    return bar.overlap(pie)
#轮播图的循环创建:
for month in list(sale.index):
    timeline.add(c_charts(month),month)
    timeline.add_schema(play_interval=1000,is_auto_play=True)
    timeline.render('轮播图.html')