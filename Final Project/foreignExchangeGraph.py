import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import datetime as dt

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/ForeignExchange.csv')
df2 = pd.read_csv('../Datasets/ForeignExchange.csv')
df3 = pd.read_csv('../Datasets/ForeignExchange.csv')

application = dash.Dash()

new_df = df1
new_df2 = df2
new_df3 = df3

dfDecade = new_df2
dfDecade['Date'] = pd.to_datetime(dfDecade['Date'])
dfCurrentDecade = dfDecade[dfDecade['Date'].dt.year >= 2010]

dfYear = new_df3
dfYear['Date'] = pd.to_datetime(dfYear['Date'])
dfCurrentYear = dfYear[dfYear['Date'].dt.year == 2019]

new_df['Date'] = pd.to_datetime(new_df['Date'])

multiline_df = new_df
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'], mode='lines', name='AUSTRALIA - AUSTRALIAN DOLLAR/US$')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['EURO AREA - EURO/US$'], mode='lines', name='EURO AREA - EURO/US$')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'], mode='lines', name='NEW ZEALAND - NEW ZELAND DOLLAR/US$')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]


# Layout
application.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
              }
              ),
    html.Div('Please select a timeframe', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-timeframe',
        options=[
            {'label': 'Year', 'value': 'Year'},
            {'label': 'Decade', 'value': 'Decade'},
            {'label': 'All time', 'value': 'All time'},
        ],
        value='Year'
    )
])

@application.callback(Output('graph1', 'figure'),              [Input('select-timeframe', 'value')])
def update_figure(selected_timeframe):
    filtered_df = multiline_df
    if(selected_timeframe == 'Year'):
        filtered_df = dfCurrentYear
    if(selected_timeframe == 'Decade'):
        filtered_df = dfCurrentDecade
    if(selected_timeframe == 'All time'):
        filtered_df = multiline_df
    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    trace1_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'],
                                  mode='lines', name='AUSTRALIA - AUSTRALIAN DOLLAR/US$')
    trace2_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['EURO AREA - EURO/US$'], mode='lines',
                                  name='EURO AREA - EURO/US$')
    trace3_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                                  mode='lines', name='NEW ZEALAND - NEW ZELAND DOLLAR/US$')
    data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]
    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_timeframe,
                                                                  xaxis={'title': 'Time'},
                                                                  yaxis={'title': 'Exchange Rate'})}

if __name__ == '__main__':
    application.run_server(debug = True, port = 8100)
