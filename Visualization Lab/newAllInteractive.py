import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/CoronaVirusTotal.csv')
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df3 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df3
barchart_df = barchart_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df = barchart_df.groupby(['NOC'])['Total'].sum().reset_index()
barchart_df = barchart_df.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack bar chart data
stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df['Unrecovered'] = stackbarchart_df['Confirmed'] - stackbarchart_df['Deaths'] - stackbarchart_df[
    'Recovered']
stackbarchart_df = stackbarchart_df[(stackbarchart_df['Country'] != 'China')]
stackbarchart_df = stackbarchart_df.groupby(['Country']).agg(
    {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()
stackbarchart_df = stackbarchart_df.sort_values(by=['Confirmed'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['Country'], y=stackbarchart_df['Unrecovered'], name='Under Treatment',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['Country'], y=stackbarchart_df['Recovered'], name='Recovered',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['Country'], y=stackbarchart_df['Deaths'], name='Deaths',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

# Line Chart
line_df = df2
line_df['Date'] = pd.to_datetime(line_df['Date'])
data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Confirmed'], mode='lines', name='Death')]

# Multi Line Chart
multiline_df = df2
multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Death'], mode='lines', name='Death')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Recovered'], mode='lines', name='Recovered')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Unrecovered'], mode='lines', name='Under Treatment')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
new_df = df4.groupby(['month']).agg(
{'average_min_temp': 'mean', 'average_max_temp': 'mean', 'actual_mean_temp': 'mean'}).reset_index()
data_bubblechart = [
go.Scatter(x=new_df['average_min_temp'],
y=new_df['average_max_temp'],
text=new_df['month'],
mode='markers',
marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_mean_temp'], showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df4['month'],
            y=df4['day'],
            z=df4['actual_max_temp'].values.tolist(),
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
        'This stack bar chart represent the CoronaVirus deaths, recovered and under treatment of all reported first 20 countries except China.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of cases'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the Corona Virus confirmed cases of all reported cases in the given period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the CoronaVirus death, recovered and under treatment cases of all reported cases in the given period.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Corona Virus Death, Recovered and under treatment Cases From 2020-01-22 to 2020-03-17',
                      xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
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