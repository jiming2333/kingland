import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 读入数据，需要更改
df = pd.read_excel('meigui.xlsx')
df = df.sort_values("累计")
v = df['各个地区'].values.tolist()
d = df['累计'].values.tolist()
# 设置颜色
color_series = ['#83A4D4', '#A1BAE0', '#5092F4', '#649173', '#2EE86C',
                '#90A9D0', '#3DBA78', '#90A9D0', '#59B077', '#1E91CA',
                '#E599C6', '#2B55A1', '#E599C6', '#44388E', '#6A368B'
                '#59B077', '#E599C6', '#C31C88', '#E599C6', '#D5225B',
                '#FF0099', '#2B5876', '#F57A34', '#FA8F2F', '#D99D21',
                '#CF7B25', '#CF7B25', '#D87171']
# 实例化Pie类
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
# 设置颜色
pie1.set_colors(color_series)
# 添加数据，设置饼图的半径，是否展示成玫瑰图
pie1.add("222", [list(z) for z in zip(v, d)],
         radius=["15%", "100%"],
         center=["50%", "60%"],
         rosetype="area"
         )
# 设置全局配置项
pie1.set_global_opts(title_opts=opts.TitleOpts(title='全球物联网报考人数'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
# 设置系列配置项
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}个", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
# 生成html文档
pie1.render("玫瑰图.html")