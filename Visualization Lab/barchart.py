import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Creating sum of total medals group by NOC Column
new_df = df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 NOC
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data - sets data location of x and y axis
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout - sets title of graph and titles of x and y axis
layout = go.Layout(title='Total medals acquired in the 2016 Olympics', xaxis_title="Countries",
                   yaxis_title="Number of total medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
