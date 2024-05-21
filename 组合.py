import pandas as pd
from pyecharts.charts import Liquid,Gauge,WordCloud,Page,Pie,Bar,Map,Timeline,Graph,Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar3D


#水球图----------------------------------------------------------------------------
data = pd.read_excel('people.xlsx')
# 元组
suitable_people = data[(data['物联网专业'] >= 23) & (data['物联网专业'] <= 25)].shape[0] / data.shape[0]
c_water = (
    Liquid(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add("lq", [suitable_people])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="物联网报考人数",pos_left='center'),
        tooltip_opts=opts.TooltipOpts(formatter="{a}: {c}%"),
        # 占位符  名称数据
    )
)
#3d--------------------------------------------------------------------------------------
env_info = pd.read_excel('3d.xlsx')
data_env = zip(env_info['Time'],env_info['Weekday'],env_info['Acceptance'])

bar3d = Bar3D(init_opts=opts.InitOpts(width='1500px',
                                      height='1000px',
                                      theme=ThemeType.ROMANTIC))
bar3d.add(series_name='学校一周录取率',
          data=list(data_env),
          xaxis3d_opts=opts.Axis3DOpts(type_='category',min_='dataMin'),
          yaxis3d_opts=opts.Axis3DOpts(type_='category'),
          zaxis3d_opts=opts.Axis3DOpts(type_='value',min_='dataMin'))

# 视觉映设配置项
bar3d.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=10,max_=40)
                      )
#仪表盘--------------------------------------------------------------------
data = pd.read_excel('yibiao.xlsx')
gau = Gauge()

gau.add(series_name='平均感受',data_pair=[('物联网专业喜爱程度',65)],
        min_=-30,max_=80,
        split_number=8,
        detail_label_opts=opts.GaugeDetailOpts(formatter='{value} %',offset_center=['0%','80%']),
        axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(0.3,'#67e0e3'),(0.7, '#37a2da'), (1, '#fd666d')], width=20)))

#玫瑰--------------------------------------------------------------------
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
# 添加数据，设置饼图的半径，是否展示成南丁格尔图
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
#饼图-----------------------------------------------------------
weather = pd.read_excel('bing.xlsx')

c_weather = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add(
        series_name="物联网从事行业",
        data_pair=[
            ("嵌入式开发工程师", int(weather['嵌入式(个)'].iloc[0])),  # 使用.iloc[0]获取Series中的第一个元素
            ("软件开发工程师", int(weather['软工(个)'].iloc[0])),
            ("硬件工程师", int(weather['硬工(个)'].iloc[0])),
            ("其他", int(weather['其他(个)'].iloc[0])),
        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="物联网从事行业", pos_left='center', pos_top='bottom'))
)

#柱状图-------------------------------------------------------------------
sale_info = pd.read_excel('zhu.xlsx',index_col=0)
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
bar.add_xaxis(list(sale_info.columns))
bar.add_yaxis("2023年报考人数", list(sale_info.iloc[0]))
bar.add_xaxis(list(sale_info.columns))
bar.add_yaxis("2024年报考人数", list(sale_info.iloc[1]))
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name='2024年报考人数总额',
        type_='value',
        position='right',
        min_=0,max_=10,
        axislabel_opts=opts.LabelOpts(formatter='{value}万元')))
#全局配置（原有的Y轴在这里配置）
bar.set_global_opts(
yaxis_opts=opts.AxisOpts(
name='2023年报考人数总额',
type_='value',
position='left',
min_=0,max_=8,
axislabel_opts=opts.LabelOpts(formatter='{value}万元')))

#折线图-----------------------------------------------------------
# 创建折线图对象
data = pd.read_excel('people.xlsx')

line_chart_co = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add_xaxis(list(data.index+1))
    .add_yaxis("物联网就业人数", data['物联网就业人数'], symbol='circle', label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="物联网就业人数增长折线图",pos_left='center'),
        xaxis_opts=opts.AxisOpts(name="日期"),
        yaxis_opts=opts.AxisOpts(name="人数", min_=0, max_=1.0),
        legend_opts=opts.LegendOpts(pos_top='top', pos_left='right')
    )
)
print(data.index)
#轮播图-------------------------------------------
sale=pd.read_excel('lunbo.xlsx',index_col=0)
timeline=Timeline()
def c_charts(month):
    bar=Bar()
    bar.add_xaxis(list(sale.columns))
    bar.add_yaxis('不同地区一年就业人数',list(sale.loc[month]),bar_width='30px')
    pie=Pie()
    pie.add('就业占比',list(zip(sale.columns,list(sale.loc[month]))),
    radius=['15%','30%'],
    center=['80%','25%'])
    return bar.overlap(pie)
for month in list(sale.index):
    timeline.add(c_charts(month),month)
    timeline.add_schema(play_interval=1000,is_auto_play=True)


# page = Page(layout=Page.DraggablePageLayout)
# page.add(c_water,bar3d,gau,pie1,c_weather,bar,line_chart_co,timeline)
# page.render('主题测试.html')
Page.save_resize_html('主题测试.html',cfg_file='chart_config.json',dest='最终主体.html')