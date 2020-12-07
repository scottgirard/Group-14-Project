import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df1
barchart_df = barchart_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df = barchart_df.groupby(['NOC'])['Total'].sum().reset_index()
barchart_df = barchart_df.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack bar chart data
new_df = df1.groupby(['NOC']).agg(
    {'Gold': 'sum', 'Silver': 'sum', 'Bronze': 'sum', 'Total': 'sum'}).reset_index()
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data_stackbarchart = [trace1, trace2, trace3]

# Line Chart
new_df = df2.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()
new_df = new_df.reindex([5, 1, 11, 10, 9, 2, 4, 3, 7, 0, 8, 6])
data_linechart = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Month')]

# Multi Line Chart
new_df = df2.groupby(['month']).agg({'actual_max_temp': 'max', 'actual_min_temp': 'min', 'actual_mean_temp': 'mean'}).reset_index()
new_df = new_df.reindex([5, 1, 11, 10, 9, 2, 4, 3, 7, 0, 8, 6])
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Max')
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='Min')
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'], mode='lines', name='Mean')
data_multiline = [trace1, trace2, trace3]


# Bubble chart
new_df = df2.groupby(['month']).agg(
{'average_min_temp': 'mean', 'average_max_temp': 'mean', 'actual_mean_temp': 'mean'}).reset_index()
data_bubblechart = [
go.Scatter(x=new_df['average_min_temp'],
y=new_df['average_max_temp'],
text=new_df['month'],
mode='markers',
marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_mean_temp'], showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df2['month'],
            y=df2['day'],
            z=df2['actual_max_temp'].values.tolist(),
            colorscale='Jet')]
layout = go.Layout(title='Maximum Temperature by Day of the Week & Month of Year', xaxis_title="Month",
                   yaxis_title="Day of the Week")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Coronavirus COVID-19 Global Cases -  1/22/2020 to 3/17/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represents the top 20 countries in total Olympic medals earned.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Total Medals Earned in the Olympics',
                                      xaxis={'title': 'Countries'}, yaxis={'title': 'Number of medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represents the total medals of the top 20 countries in the 2016 Olympics.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Total Medals of Top 20 Countries in the 2016 Olympics',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Total medals'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the absolute maximum temperatures for each month of the year.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Maximum Temperatures for Each Month of the Year',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Actual Max Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represents the max, min, and mean temperatures of each month of the year.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Actual Max, Min, and Mean temp by Month',
                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the average min, average max, and mean temps of each month.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Month Temperatures',
                                      xaxis={'title': 'Average Min Temps'}, yaxis={'title': 'Average Max Temps'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represents the hottest days recorded of each day of the week in each month.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Hottest Temperatures Recorded',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Day of Week'})
              }
              )
])

if __name__ == '__main__':
    app.run_server(debug = True, port = 8250)