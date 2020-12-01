import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#load csv from datasets folder

df = pd.read_csv('../Datasets/Weather2014-15.csv')

#preparing data
data = [go.Heatmap(x=df['month'],
            y=df['day'],
            z=df['actual_max_temp'].values.tolist(),
            colorscale='Jet')]

#preparing layout

layout = go.Layout(title='Maximum Temperature by Day of the Week & Month of Year', xaxis_title="Month",
                   yaxis_title="Day of the Week")

#plot the figure and saving in a html file

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
