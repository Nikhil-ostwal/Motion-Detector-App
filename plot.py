from motion_detctor import df
import bokeh
from bokeh.plotting import figure, output_file
from bokeh.models import HoverTool , ColumnDataSource
from bokeh.io import show

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(plot_width=800, plot_height=300, title="Motion Graph",x_axis_type='datetime', toolbar_location=None, tools="")

p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1

q = p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)
 
hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

output_file("Graph.html")
show(p)
