import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating max temperature group by month Column
df = df.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()

# Reorder the dataframe rows to match original data
df = df.reindex([5, 1, 11, 10, 9, 2, 4, 3, 7, 0, 8, 6])

# Preparing data
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Month')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperature by Month', xaxis_title="Month",
                   yaxis_title="Actual Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weather_line_chart.html')