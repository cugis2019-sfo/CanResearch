import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

#plot([cancercases])

##we read the data into a dataset or dataframe called df
df = pd.read_excel("GISdata.xlsx", sheet_name= "cancercases")

#we use the Bar graph option of the graph_objs function from the plotly library
cancercases=go.Bar(x=df["CancerType"], y=df["Number"],

#we add the color to the graph using the jet scale
        marker={"color": df["Number"], "colorscale" : "Portland"}
          )

#we use the layout option of the graph_objs from the plotly library
titles= go.Layout(
        #define the title of the graph
        title= "Cancer Cases Found in Women",
        
        #define title for the x-axis
        xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                        text="Cancer Types",
                        )
                ),
                
                #define title for y-axis
                yaxis=go.layout.YAxis(
                        title=go.layout.yaxis.Title(
                                text="Number",
                                )
                        )
                )

fig = go.Figure(data=[cancercases],layout=titles)
plot(fig)

















