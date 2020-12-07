import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating max, min, mean temperature group by month Column
df1 = df.groupby(['month']).agg({'actual_max_temp': 'max', 'actual_min_temp': 'min', 'actual_mean_temp': 'mean'}).reset_index()

# Reorder the dataframe rows to match original data
df1 = df1.reindex([5, 1, 11, 10, 9, 2, 4, 3, 7, 0, 8, 6])

# Preparing data
trace1 = go.Scatter(x=df1['month'], y=df1['actual_max_temp'], mode='lines', name='Max')
trace2 = go.Scatter(x=df1['month'], y=df1['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=df1['month'], y=df1['actual_mean_temp'], mode='lines', name='Mean')
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Actual Max, Min, and Mean Temperature by Month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weather_multi_line_chart.html')