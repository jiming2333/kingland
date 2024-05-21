import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
weather = pd.read_excel('bing.xlsx')
#初始化饼图对象 这里使用Pie类来创建一个饼图对象，并通过InitOpts类来设置初始化选项。theme=ThemeType.MACARONS表示使用“MACARONS”主题来渲染图表。
c_weather = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    #添加数据系列：在.add()方法中，定义了饼图的数据系列。series_name是系列的名称，这里设置为“物联网从事行业”。
    .add(
        series_name="物联网从事行业",
        #data_pair是一个列表，包含了每个行业及其对应的从业者数量。
        # 这些数据从weather这个DataFrame中通过列名（如'嵌入式(个)'、'软工(个)'等）和.iloc[0]（用于获取每列的第一个元素）来获取，并且转换为整数类型。
        data_pair=[
            ("嵌入式开发工程师", int(weather['嵌入式(个)'].iloc[0])),  # 使用.iloc[0]获取Series中的第一个元素
            ("软件开发工程师", int(weather['软工(个)'].iloc[0])),
            ("硬件工程师", int(weather['硬工(个)'].iloc[0])),
            ("其他", int(weather['其他(个)'].iloc[0])),
        ],
    )
    #设置全局选项：使用.set_global_opts()方法来设置全局选项。这里只设置了标题选项title_opts，
    # 标题为“物联网从事行业”，并且设置了标题的位置，使其位于图表的左中部和底部。
    .set_global_opts(title_opts=opts.TitleOpts(title="物联网从事行业", pos_left='center', pos_top='bottom'))
)
#将饼图对象赋值给变量
c_weather.render('饼图.html')
