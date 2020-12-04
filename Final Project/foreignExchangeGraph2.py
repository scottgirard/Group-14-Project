import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import datetime as dt

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/ForeignExchange.csv')
#df2 = pd.read_csv('../Datasets/ForeignExchange.csv')
#df3 = pd.read_csv('../Datasets/ForeignExchange.csv')

application = dash.Dash()

new_df = df1
#new_df2 = df2
#new_df3 = df3

#dfDecade = new_df2
#dfDecade['Date'] = pd.to_datetime(dfDecade['Date'])
#dfCurrentDecade = dfDecade[dfDecade['Date'].dt.year >= 2010]

#dfYear = new_df3
#dfYear['Date'] = pd.to_datetime(dfYear['Date'])
#dfCurrentYear = dfYear[dfYear['Date'].dt.year == 2019]

new_df['Date'] = pd.to_datetime(new_df['Date'])

multiline_df = new_df
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'], mode='lines', name='AUSTRALIA - AUSTRALIAN DOLLAR/US$')
data_multiline = [trace1_multiline]


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
    html.Div('Please select a currency', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-currency',
        options=[
            {'label': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
            {'label': 'EURO AREA - EURO/US$', 'value': 'EURO AREA - EURO/US$'},
            {'label': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
            {'label': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
            {'label': 'BRAZIL - REAL/US$', 'value': 'BRAZIL - REAL/US$'},
            {'label': 'CANADA - CANADIAN DOLLAR/US$', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
            {'label': 'CHINA - YUAN/US$', 'value': 'CHINA - YUAN/US$'},
            {'label': 'HONG KONG - HONG KONG DOLLAR/US$', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
            {'label': 'INDIA - INDIAN RUPEE/US$', 'value': 'INDIA - INDIAN RUPEE/US$'},
            {'label': 'KOREA - WON/US$', 'value': 'KOREA - WON/US$'},
            {'label': 'MEXICO - MEXICAN PESO/US$', 'value': 'MEXICO - MEXICAN PESO/US$'},
            {'label': 'SOUTH AFRICA - RAND/US$', 'value': 'SOUTH AFRICA - RAND/US$'},
            {'label': 'SINGAPORE - SINGAPORE DOLLAR/US$', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
            {'label': 'DENMARK - DANISH KRONE/US$', 'value': 'DENMARK - DANISH KRONE/US$'},
            {'label': 'JAPAN - YEN/US$', 'value': 'JAPAN - YEN/US$'},
            {'label': 'MALAYSIA - RINGGIT/US$', 'value': 'MALAYSIA - RINGGIT/US$'},
            {'label': 'NORWAY - NORWEGIAN KRONE/US$', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
            {'label': 'SWEDEN - KRONA/US$', 'value': 'SWEDEN - KRONA/US$'},
            {'label': 'SRI LANKA - SRI LANKAN RUPEE/US$', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
            {'label': 'SWITZERLAND - FRANC/US$', 'value': 'SWITZERLAND - FRANC/US$'},
            {'label': 'TAIWAN - NEW TAIWAN DOLLAR/US$', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
            {'label': 'THAILAND - BAHT/US$', 'value': 'THAILAND - BAHT/US$'},
        ],
        value='AUSTRALIA - AUSTRALIAN DOLLAR/US$'
    )
])

@application.callback(Output('graph1', 'figure'),              [Input('select-currency', 'value')])
def update_figure(selected_currency):
    country = selected_currency
    trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df[country],
                                  mode='lines', name=country)
    data_multiline = [trace1_multiline]
    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_currency,
                                                                  xaxis={'title': 'Time'},
                                                                  yaxis={'title': 'Exchange Rate'})}

if __name__ == '__main__':
    application.run_server(debug = True, port = 8150)
