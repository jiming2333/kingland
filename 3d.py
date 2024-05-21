from pyecharts.charts import Bar3D
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd
#一个Excel文件（'3d.xlsx'）中读取数据
env_info = pd.read_excel('3d.xlsx')
#使用zip函数将DataFrame中的三列（'Time', 'Weekday', 'Acceptance'）组合成一个元组的迭代器。
data_env = zip(env_info['Time'],env_info['Weekday'],env_info['Acceptance'])
#创建3D柱状图:置了图表的初始选项，如宽度、高度和主题。
bar3d = Bar3D(init_opts=opts.InitOpts(width='1500px',
                                      height='1000px',
                                      theme=ThemeType.ROMANTIC))
#添加数据到3D柱状图:      设置3D轴的选项:min_='dataMin'表示该轴的最小值将自动设置为数据中的最小值。
bar3d.add(series_name='学校一周录取率',
          data=list(data_env),
          xaxis3d_opts=opts.Axis3DOpts(type_='category',min_='dataMin'),
          yaxis3d_opts=opts.Axis3DOpts(type_='category'),
          zaxis3d_opts=opts.Axis3DOpts(type_='value',min_='dataMin'))

# 视觉映设配置项
bar3d.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=10,max_=40)
                      )
bar3d.render('3D柱状图.html')

