import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType

dl = pd.read_excel("DL.xlsx",header=0)
m = Map()
m = Map(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
m.add(series_name='大连各区人口分布情况',maptype='world',data_pair=list(zip(dl['区县'],dl['人口（万人）'])),
      )
m.set_global_opts(title_opts=opts.TitleOpts(title="大连各区人口分布情况",pos_right="70%"),
                  visualmap_opts=opts.VisualMapOpts(),
                  )
m.render('map.html')