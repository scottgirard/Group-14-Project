import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Data from data set is received
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['month']).agg(
{'average_min_temp': 'mean', 'average_max_temp': 'mean', 'actual_mean_temp': 'mean'}).reset_index()

# Preparing data - sets information to be used in each axis, the mode in which info will be displayed, and sets size and color of bubbles
data = [
go.Scatter(x=new_df['average_min_temp'],
y=new_df['average_max_temp'],
text=new_df['month'],
mode='markers',
marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_mean_temp'], showscale=True))
]

# Preparing layout - sets title of graph and title of axes
layout = go.Layout(title='2014-15 Weather Statistics', xaxis_title="Minimum Average Temperature",
yaxis_title="Maximum Average Temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')