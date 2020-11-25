import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data
data = [
go.Scatter(x=df['average_min_temp'],
y=df['average_max_temp'],
text=df['month'],
mode='markers',
marker=dict(size=df['actual_mean_temp'] / 5,color=df['actual_mean_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='2014-15 Weather Statistics', xaxis_title="Minimum Average Temperature",
yaxis_title="Maximum Average Temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')