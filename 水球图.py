import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import ThemeType

data = pd.read_excel('people.xlsx')
# 元组        '物联网专业'列中筛选出100人里选择物联网专业人数
suitable_people = data[(data['物联网专业'] >= 23) & (data['物联网专业'] <= 25)].shape[0] / data.shape[0]
#创建液态进度条图表
c_water = (
   # 创建一个 Liquid 图表对象，并指定初始化选项（这里设置了主题为 MACARONS）

    Liquid(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
   # 添加一个系列到图表中，系列名为 "lq"，数据为 [suitable_people]
    # 这里 suitable_people 应该是之前计算出的一个百分比值
    .add("lq", [suitable_people])
    # 设置图表的全局选项
    .set_global_opts(
        # 设置图表的标题，标题为 "物联网报考人数"，并且标题的位置在中心
        title_opts=opts.TitleOpts(title="物联网报考人数占比",pos_left='center'),
        # 在这里，{c} 将被替换为 suitable_people 的值，但会加上一个百分号（%）
        tooltip_opts=opts.TooltipOpts(formatter="{a}: {c}%"),
        # 占位符  名称数据
    )
)

c_water.render('水球图.html')