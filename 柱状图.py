import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
#读取Excel文件:这行代码使用pandas的read_excel函数读取了一个名为'zhu.xlsx'的Excel文件，并将第一列设置为索引。
sale_info = pd.read_excel('zhu.xlsx',index_col=0)
#初始化柱状图对象:这行代码创建了一个柱状图对象，并设置了主题为'CHALK'。
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
#添加X轴和Y轴数据:
bar.add_xaxis(list(sale_info.columns))
bar.add_yaxis("2023年报考人数", list(sale_info.iloc[0]))
bar.add_xaxis(list(sale_info.columns))
bar.add_yaxis("2024年报考人数", list(sale_info.iloc[1]))
#扩展Y轴：这行代码为图表添加了一个右侧的Y轴，并设置了它的名称、类型、位置、最小值和最大值，以及标签的格式化选项
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name='2024年报考人数总额',
        type_='value',
        position='right',
        min_=0,max_=10,
        axislabel_opts=opts.LabelOpts(formatter='{value}万元')))
#全局配置（原有的Y轴在这里配置）
# 这行代码为左侧的Y轴设置了名称、类型、位置、最小值和最大值，
# 以及标签的格式化选项。但是，因为已经调用了extend_axis来扩展Y轴，所以这里实际上是为左侧的Y轴（默认Y轴）进行的配置。
bar.set_global_opts(
yaxis_opts=opts.AxisOpts(
name='2023年报考人数总额',
type_='value',
position='left',
min_=0,max_=8,
axislabel_opts=opts.LabelOpts(formatter='{value}万元')))

bar.render('柱状图.html')