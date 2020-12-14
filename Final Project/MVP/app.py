import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
from html import unescape
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css']
# external_stylesheets = ['http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css']
# external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, serve_locally=False)
server = app.server

# Global Variables
from_conversion_symbol = 'USD'
to_conversion_symbol = 'USD'
amount_value: float = 0.0
converted_value: float = 0.0
message = ""
selected_currency = ""

# Load CSV file from Datasets folder
df1 = new_df = new_df2 = pd.read_csv('ForeignExchange.csv') #df2

dfDecade = df1
dfDecade['Date'] = pd.to_datetime(dfDecade['Date'])
dfCurrentDecade = dfDecade[dfDecade['Date'].dt.year >= 2010]

dfYear = df1
dfYear['Date'] = pd.to_datetime(dfYear['Date'])
dfCurrentYear = dfYear[dfYear['Date'].dt.year == 2019]

new_df['Date'] = pd.to_datetime(new_df['Date'])

multiline_df = df1

trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'], mode='lines',
                              name='AUD/US$')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['EURO AREA - EURO/US$'], mode='lines',
                              name='EUR/US$')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                              mode='lines', name='NZD/US$')
trace4_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                              mode='lines', name='GBP/US$')
trace5_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['BRAZIL - REAL/US$'],
                              mode='lines', name='BRL/US$')
trace6_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['CANADA - CANADIAN DOLLAR/US$'],
                              mode='lines', name='CAD/US$')
trace7_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['CHINA - YUAN/US$'],
                              mode='lines', name='CNY/US$')
trace8_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['HONG KONG - HONG KONG DOLLAR/US$'],
                              mode='lines', name='HKD/US$')
trace9_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['INDIA - INDIAN RUPEE/US$'],
                              mode='lines', name='INR/US$')
trace10_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['KOREA - WON/US$'],
                              mode='lines', name='KRW/US$')
trace11_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['MEXICO - MEXICAN PESO/US$'],
                              mode='lines', name='MXN/US$')
trace12_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['SOUTH AFRICA - RAND/US$'],
                              mode='lines', name='ZAR/US$')
trace13_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['SINGAPORE - SINGAPORE DOLLAR/US$'],
                              mode='lines', name='SGD/US$')
trace14_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['DENMARK - DANISH KRONE/US$'],
                              mode='lines', name='DKK/US$')
trace15_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['JAPAN - YEN/US$'],
                              mode='lines', name='JPY/US$')
trace16_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['MALAYSIA - RINGGIT/US$'],
                              mode='lines', name='MYR/US$')
trace17_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['NORWAY - NORWEGIAN KRONE/US$'],
                              mode='lines', name='NOK/US$')
trace18_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['SWEDEN - KRONA/US$'],
                              mode='lines', name='SEK/US$')
trace19_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['SRI LANKA - SRI LANKAN RUPEE/US$'],
                              mode='lines', name='LKR/US$')
trace20_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['SWITZERLAND - FRANC/US$'],
                              mode='lines', name='CHF/US$')
trace21_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['TAIWAN - NEW TAIWAN DOLLAR/US$'],
                              mode='lines', name='TWD/US$')
trace22_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['THAILAND - BAHT/US$'],
                              mode='lines', name='THB/US$')

data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline, trace4_multiline,
                  trace5_multiline, trace6_multiline, trace7_multiline, trace8_multiline,
                  trace11_multiline, trace12_multiline,
                  trace13_multiline,trace14_multiline, trace16_multiline,
                  trace17_multiline, trace18_multiline, trace20_multiline,]

data_duoline = [trace1_multiline, trace2_multiline]

# Get the conversion rate for the currencies (most recent data)
df_aud = df1['AUSTRALIA - AUSTRALIAN DOLLAR/US$'].iloc[-1]
df_eur = df1['EURO AREA - EURO/US$'].iloc[-1]
df_nzd = df1['NEW ZEALAND - NEW ZELAND DOLLAR/US$'].iloc[-1]
df_gbp = df1['UNITED KINGDOM - UNITED KINGDOM POUND/US$'].iloc[-1]
df_brl = df1['BRAZIL - REAL/US$'].iloc[-1]
df_cad = df1['CANADA - CANADIAN DOLLAR/US$'].iloc[-1]
df_cny = df1['CHINA - YUAN/US$'].iloc[-1]
df_hkd = df1['HONG KONG - HONG KONG DOLLAR/US$'].iloc[-1]
df_inr = df1['INDIA - INDIAN RUPEE/US$'].iloc[-1]
df_krw = df1['KOREA - WON/US$'].iloc[-1]
df_mxn = df1['MEXICO - MEXICAN PESO/US$'].iloc[-1]
df_zar = df1['SOUTH AFRICA - RAND/US$'].iloc[-1]
df_sgd = df1['SINGAPORE - SINGAPORE DOLLAR/US$'].iloc[-1]
df_dkk = df1['DENMARK - DANISH KRONE/US$'].iloc[-1]
df_jpy = df1['JAPAN - YEN/US$'].iloc[-1]
df_myr = df1['MALAYSIA - RINGGIT/US$'].iloc[-1]
df_nok = df1['NORWAY - NORWEGIAN KRONE/US$'].iloc[-1]
df_sek = df1['SWEDEN - KRONA/US$'].iloc[-1]
df_lkr = df1['SRI LANKA - SRI LANKAN RUPEE/US$'].iloc[-1]
df_chf = df1['SWITZERLAND - FRANC/US$'].iloc[-1]
df_twd = df1['TAIWAN - NEW TAIWAN DOLLAR/US$'].iloc[-1]
df_thb = df1['THAILAND - BAHT/US$'].iloc[-1]
df_usd = 1.0

data_frame_label = {
                    'AUSTRALIA - AUSTRALIAN DOLLAR/US$':'Australian Dollar',
                    'EURO AREA - EURO/US$':'Euro Members',
                    'NEW ZEALAND - NEW ZELAND DOLLAR/US$':'New Zealand Dollar',
                    'UNITED KINGDOM - UNITED KINGDOM POUND/US$':'United Kingdom Pound',
                    'BRAZIL - REAL/US$':'Brazil Real',
                    'CANADA - CANADIAN DOLLAR/US$':'Canada Dollar',
                    'CHINA - YUAN/US$':'China Yuan',
                    'HONG KONG - HONG KONG DOLLAR/US$':'Hong Kong Dollar',
                    'INDIA - INDIAN RUPEE/US$':'India Rupee',
                    'KOREA - WON/US$':'South Korea Won',
                    'MEXICO - MEXICAN PESO/US$':'Mexico Peso',
                    'SOUTH AFRICA - RAND/US$':'South Africa Rand',
                    'SINGAPORE - SINGAPORE DOLLAR/US$':'Singapore Dollar',
                    'DENMARK - DANISH KRONE/US$':'Denmark Krone',
                    'JAPAN - YEN/US$':'Japan' + unescape('&nbsp;') + 'Yen',
                    'MALAYSIA - RINGGIT/US$':'Malaysia Ringgit',
                    'NORWAY - NORWEGIAN KRONE/US$':'Norway Krone',
                    'SWEDEN - KRONA/US$':'Sweden Krona',
                    'SRI LANKA - SRI LANKAN RUPEE/US$':'Sri Lanka Rupee',
                    'SWITZERLAND - FRANC/US$':'Switzerland Franc',
                    'TAIWAN - NEW TAIWAN DOLLAR/US$':'Taiwan New Dollar',
                    'THAILAND - BAHT/US$':'Thailand Baht',
                    }

conversion_dict = {
                    'AUD':df_aud, 'BRL':df_brl, 'CAD':df_cad, 'CHF':df_chf, 'CNY':df_cny,
                    'DKK':df_dkk, 'EUR':df_eur, 'GBP':df_gbp, 'HKD':df_hkd, 'INR':df_inr,
                    'JPY':df_jpy, 'KRW':df_krw, 'LKR':df_lkr, 'MXN':df_mxn, 'MYR':df_myr,
                    'NOK':df_nok, 'NZD':df_nzd, 'SGD':df_sgd, 'ZAR':df_zar, 'SEK':df_sek,
                    'THB':df_thb, 'TWD':df_twd, 'USD':df_usd,
                   }

long_name_dict = {
                    'AUD':'Australian Dollar', 'BRL':'Brazil Real',     'CAD':'Canada Dollar',
                    'CHF':'Switzerland Franc', 'CNY':'China Yuan',      'DKK':'Denmark Krone',
                    'EUR':'Euro Members',      'GBP':'United Kingdom Pound',
                    'HKD':'Hong Kong Dollar',  'INR':'India Rupee',     'JPY':'Japan' + unescape('&nbsp;') + 'Yen',
                    'KRW':'South Korea Won',   'LKR':'Sri Lanka Rupee', 'MXN':'Mexico Peso',
                    'MYR':'Malaysia Ringgit',  'NOK':'Norway Krone',    'NZD':'New Zealand Dollar',
                    'SGD':'Singapore Dollar',  'ZAR':'South Africa Rand',
                    'SEK':'Sweden Krona',      'THB':'Thailand Baht',   'TWD':'Taiwan New Dollar',
                    'USD':'U.S. Dollar',
                }

dropdown_options = [
                    {'label': 'Australian Dollar', 'value': 'AUD'},
                    {'label': 'Brazil Real', 'value': 'BRL'},
                    {'label': 'Canada Dollar', 'value': 'CAD'},
                    {'label': 'China Yuan', 'value': 'CNY'},
                    {'label': 'Denmark Krone', 'value': 'DKK'},
                    {'label': 'Euro Members', 'value': 'EUR'},
                    {'label': 'Hong Kong Dollar', 'value': 'HKD'},
                    {'label': 'India Rupee', 'value': 'INR'},
                    {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JPY'},
                    {'label': 'Malaysia Ringgit', 'value': 'MYR'},
                    {'label': 'Mexico Peso', 'value': 'MXN'},
                    {'label': 'New Zealand Dollar', 'value': 'NZD'},
                    {'label': 'Norway Krone', 'value': 'NOK'},
                    {'label': 'Singapore Dollar', 'value': 'SGD'},
                    {'label': 'South Africa Rand', 'value': 'ZAR'},
                    {'label': 'South Korea Won', 'value': 'KRW'},
                    {'label': 'Sri Lanka Rupee', 'value': 'LKR'},
                    {'label': 'Sweden Krona', 'value': 'SEK'},
                    {'label': 'Switzerland Franc', 'value': 'CHF'},
                    {'label': 'Taiwan New Dollar', 'value': 'TWD'},
                    {'label': 'Thailand Baht', 'value': 'THB'},
                    {'label': 'United Kingdom Pound', 'value': 'GBP'},
                    {'label': 'U.S. Dollar', 'value': 'USD'},
                   ]



app.layout = html.Div([
    html.Div(style={'text-align': 'center'}, children=[
    html.I(className='fa d-block fa-bullseye fa-5x mb-4 text-info'),
    html.H2('Foreign Currency Exchange', style={'color': '#559C3E'}),
    ]),

    html.H6('Convert from:', style={'color': '#559C3E'}),
    dcc.Dropdown(
        id='convert_from-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_from-output-container'),

    html.H6('Convert to:', style={'color': '#559C3E'}),
    dcc.Dropdown(
        id='convert_to-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_to-output-container'),

    html.H6('Amount', style={'color': '#559C3E'}),
    dcc.Input(
        id='num-amount',
        type='number',
        debounce=False,
        placeholder=0.00,
    ),

    html.H5(id='message_container', style={'color': '#559C3E', 'margin': '10px'}),
    html.Hr(),

    html.H6('All Currencies:', style={'color': '#559C3E'}),
    html.Div(className='row', children=[
    html.Div(style={'display': 'inline-block'}, className='six columns', children=[
    html.Table([
        html.Tr([html.Td(html.H6('Currency', style={'color': '#3C77AF'})), html.Td(html.H6('Symbols', style={'color': '#3C77AF'})),
        html.Td(html.H6(' ')), html.Td(html.H6('Value', style={'color': '#3C77AF'}))]),
        html.Tr([html.Td('Australia Dollar'), html.Td('AUD'), html.Td('A' + unescape('&#36;')), html.Td(id='aud')]),
        html.Tr([html.Td('Brazil Real'), html.Td(['BRL', ]), html.Td('R'+ unescape('&#36;')), html.Td(id='brl')]),
        html.Tr([html.Td('Canada Dollar'), html.Td(['CAD', ]), html.Td('C'+ unescape('&#36;')), html.Td(id='cad')]),
        html.Tr([html.Td('China Yuan'), html.Td(['CNY', ]), html.Td(unescape('&#20803;')), html.Td(id='cny')]),
        html.Tr([html.Td('Denmark Krone'), html.Td(['DKK', ]), html.Td('kr'), html.Td(id='dkk')]),
        html.Tr([html.Td('Euro Members'), html.Td(['EUR', ]), html.Td(unescape('&#8364;')), html.Td(id='eur')]),
        html.Tr([html.Td('Hong Kong Dollar'), html.Td(['HKD', ]), html.Td('HK' + unescape('&#36;')), html.Td(id='hkd')]),
        html.Tr([html.Td('India Rupee'), html.Td(['INR', ]), html.Td(unescape('&#8377;')), html.Td(id='inr')]),
        html.Tr([html.Td('Japan Yen'), html.Td(['JPY', ]), html.Td(unescape('&#165;')), html.Td(id='jpy')]),
        html.Tr([html.Td('Malaysia Ringgit'), html.Td(['MYR', ]), html.Td('RM'), html.Td(id='myr')]),
        html.Tr([html.Td('Mexico Peso'), html.Td(['MXN', ]), html.Td('Mex' + unescape('&#36;')), html.Td(id='mxn')]),
        html.Tr(
        [html.Td('New Zealand Dollar'), html.Td(['NZD', ]), html.Td('NZ' + unescape('&#36;')), html.Td(id='nzd')]),
        ]),
    ]),
    html.Div(className='five columns', children=[
    html.Table([
        html.Tr([html.Td(html.H6('Currency', style={'color': '#3C77AF'})), html.Td(html.H6('Symbols', style={'color': '#3C77AF'})),
        html.Td(html.H6(' ')), html.Td(html.H6('Value', style={'color': '#3C77AF'}))]),
        html.Tr([html.Td('Norway Krone'), html.Td(['NOK', ]), html.Td('kr'), html.Td(id='nok')]),
        html.Tr([html.Td('Singapore Dollar'), html.Td(['SGD', ]), html.Td('S' + unescape('&#36;')), html.Td(id='sgd')]),
        html.Tr([html.Td('South Africa Rand'), html.Td(['ZAR', ]), html.Td('R'), html.Td(id='zar')]),
        html.Tr([html.Td('South Korea Won'), html.Td(['KRW', ]), html.Td(unescape('&#8361;')), html.Td(id='krw')]),
        html.Tr([html.Td('Sri Lanka Rupee'), html.Td(['LKR', ]), html.Td('Rs'), html.Td(id='lkr')]),
        html.Tr([html.Td('Sweden Krona'), html.Td(['SEK', ]), html.Td('kr'), html.Td(id='sek')]),
        html.Tr([html.Td('Switzerland Franc'), html.Td(['CHF', ]), html.Td('fr'), html.Td(id='chf')]),
        html.Tr([html.Td('Taiwan New Dollar'), html.Td(['TWD', ]), html.Td('NT' + unescape('&#36;')), html.Td(id='twd')]),
        html.Tr([html.Td('Thailand Baht'), html.Td(['THB', ]), html.Td(unescape('&#3647;')), html.Td(id='thb')]),
        html.Tr([html.Td('United Kingdom Pound'), html.Td(['GBP', ]), html.Td(unescape('&#163;')), html.Td(id='gbp')]),
        html.Tr([html.Td('U.S. Dollar'), html.Td(['USD', ]), html.Td('$'), html.Td(id='usd')]),
        ]),
    ]),
    ]),

########################### First Graph #############################

    html.Hr(),
    html.H3('High Level Overview', style={'color': '#559C3E'}),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
              }
              ),

    html.Div('Please select a timeframe', style={'color': '#F7B02', 'margin': '10px'}),
    dcc.Dropdown(
        id='select-timeframe',
        options=[
            {'label': 'Year', 'value': 'Year'},
            {'label': 'Decade', 'value': 'Decade'},
            {'label': 'All time', 'value': 'All time'},
        ],
        value='Year'
    ),
    html.Hr(),

html.H3('Single Currency Focus', style={'color': '#559C3E'}),
dcc.Graph(id='graph2',
          figure={
              'data': data_multiline,
              'layout': go.Layout(
                  title='Foreign Exchange Rate 2000-2019',
                  xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
          }
          ),
html.Div('Please select a currency', style={'color': '#F7B02', 'margin': '10px'}),
dcc.Dropdown(
    id='select-currency',
    placeholder="Select a currency",
    options=[
         {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
         {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
         {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
         {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
         {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
         {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
         {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
         {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
         {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
         {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
         {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
         {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
         {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
         {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
         {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
         {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
         {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
         {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
         {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
         {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
         {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
         {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
    ],
    value='AUSTRALIA - AUSTRALIAN DOLLAR/US$',
    ),

#################### Begin Third Graph #######################

    html.Hr(),
    html.H3('Currency Comparison', style={'color': '#559C3E'}),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_duoline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'}),
              }
              ),
    html.Div('Please select a first country to compare.', style={'color': '#F7B02', 'margin': '10px'}),
    dcc.Dropdown(
        id='comparison1',
        placeholder="Select a currency",
        options=[
            {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
            {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
            {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
            {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
            {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
            {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
            {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
            {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
            {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
            {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
            {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
            {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
            {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
            {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
            {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
            {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
            {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
            {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
            {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
            {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
            {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
            {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
        ],
        value='AUSTRALIA - AUSTRALIAN DOLLAR/US$'
    ),
    html.Div('Please select a second country to compare.', style={'color': '#F7B02', 'margin': '10px'}),
    dcc.Dropdown(
        id='comparison2',
        placeholder="Select a currency",
        options=[
            {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
            {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
            {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
            {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
            {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
            {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
            {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
            {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
            {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
            {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
            {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
            {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
            {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
            {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
            {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
            {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
            {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
            {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
            {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
            {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
            {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
            {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
        ],
        value='EURO AREA - EURO/US$'
    ),
    html.Div('Please enter a year between 2000 and 2019 to filter timeframe of the graph.', style={'color': '#F7B02', 'margin': '10px'}),
    html.Div(dcc.Input(id='timeframe2', type='text')),
    html.Br(),
    html.Button('Submit', id='button'),
    html.Br(),
    html.Br()
])

#################### End Third Graph #########################

@app.callback(
    Output('aud', 'children'),
    Output('brl', 'children'),
    Output('cad', 'children'),
    Output('cny', 'children'),
    Output('dkk', 'children'),
    Output('eur', 'children'),
    Output('hkd', 'children'),
    Output('inr', 'children'),
    Output('jpy', 'children'),
    Output('myr', 'children'),
    Output('mxn', 'children'),
    Output('nzd', 'children'),
    Output('nok', 'children'),
    Output('sgd', 'children'),
    Output('zar', 'children'),
    Output('krw', 'children'),
    Output('lkr', 'children'),
    Output('sek', 'children'),
    Output('chf', 'children'),
    Output('twd', 'children'),
    Output('thb', 'children'),
    Output('gbp', 'children'),
    Output('usd', 'children'),
    Input('num-amount', 'value'))
def callback_a(x):
    global amount_value
    amount_value = x
    if x is None:
        raise PreventUpdate
    else:
        return round(x / conversion_dict[from_conversion_symbol] * df_aud, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_brl, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_cad, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_cny, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_dkk, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_eur, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_hkd, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_inr, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_jpy, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_myr, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_mxn, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_nzd, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_nok, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_sgd, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_zar, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_krw, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_lkr, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_sek, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_chf, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_twd, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_thb, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_gbp, 2), \
            round(x / conversion_dict[from_conversion_symbol] * df_usd, 2),

@app.callback(
    Output('convert_from-output-container', 'children'),
    Output('num-amount', 'value'),
    Input('convert_from-dropdown', 'value')
)
def update_convert_from(value):
    if value is None:
        raise PreventUpdate
    else:
        global from_conversion_symbol
        from_conversion_symbol = value
    # return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2)), amount_value]
    return['', amount_value]


@app.callback(
    Output('convert_to-output-container', 'children'),
    # Output('num-amount', 'value'),
    Input('convert_to-dropdown', 'value')
)
def update_convert_to(value):
    if value is None:
        raise PreventUpdate
    else:
        global to_conversion_symbol
        to_conversion_symbol = value
    # return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2))]
    return['', '']

@app.callback(
    Output('message_container', 'children'),
    Input('convert_to-dropdown', 'value'),
    Input('num-amount', 'value')
)
def update_message(value, value2):
    if amount_value is None:
        raise PreventUpdate
    else:
        global message
        message = ['{} {} is equivalent to {} {}'.format(amount_value,
            long_name_dict[from_conversion_symbol], # from_conversion_symbol,
            round(amount_value / conversion_dict[from_conversion_symbol] * conversion_dict[to_conversion_symbol], 2),
            long_name_dict[to_conversion_symbol])] # to_conversion_symbol)]
        return message

######################### Second Graph Callback ##############################

@app.callback(Output('graph2', 'figure'), [Input('select-currency', 'value')])
def update_figure2(selected_currency):
    if selected_currency is None:
        raise PreventUpdate
    else:
        country = selected_currency
        trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df[country],
                                  mode='lines', name=data_frame_label[country])
        data_multiline = [trace1_multiline]

    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + data_frame_label[selected_currency],
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}

######################### First Graph Callback ##############################

@app.callback(Output('graph1', 'figure'), [Input('select-timeframe', 'value')])
def update_figure1(selected_timeframe):
    if selected_timeframe is None:
        raise PreventUpdate
    else:
        filtered_df = multiline_df

    if (selected_timeframe == 'Year'):
        filtered_df = dfCurrentYear
    if (selected_timeframe == 'Decade'):
        filtered_df = dfCurrentDecade
    if (selected_timeframe == 'All time'):
        filtered_df = multiline_df

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    trace1_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'],
                                  mode='lines',
                                  name='AUD/US$')
    trace2_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['EURO AREA - EURO/US$'], mode='lines',
                                  name='EUR/US$')
    trace3_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                                  mode='lines', name='NZD/US$')
    trace4_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                                  mode='lines', name='GBP/US$')
    trace5_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['BRAZIL - REAL/US$'],
                                  mode='lines', name='BRL/US$')
    trace6_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['CANADA - CANADIAN DOLLAR/US$'],
                                  mode='lines', name='CAD/US$')
    trace7_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['CHINA - YUAN/US$'],
                                  mode='lines', name='CNY/US$')
    trace8_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['HONG KONG - HONG KONG DOLLAR/US$'],
                                  mode='lines', name='HKD/US$')
    # trace9_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['INDIA - INDIAN RUPEE/US$'],
    #                               mode='lines', name='INR/US$')
    # trace10_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['KOREA - WON/US$'],
    #                                mode='lines', name='KRW/US$')
    trace11_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['MEXICO - MEXICAN PESO/US$'],
                                   mode='lines', name='MXN/US$')
    trace12_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['SOUTH AFRICA - RAND/US$'],
                                   mode='lines', name='ZAR/US$')
    trace13_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['SINGAPORE - SINGAPORE DOLLAR/US$'],
                                   mode='lines', name='SGD/US$')
    trace14_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['DENMARK - DANISH KRONE/US$'],
                                   mode='lines', name='DKK/US$')
    # trace15_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['JAPAN - YEN/US$'],
    #                                mode='lines', name='JPY/US$')
    trace16_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['MALAYSIA - RINGGIT/US$'],
                                   mode='lines', name='MYR/US$')
    trace17_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['NORWAY - NORWEGIAN KRONE/US$'],
                                   mode='lines', name='NOK/US$')
    trace18_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['SWEDEN - KRONA/US$'],
                                   mode='lines', name='SEK/US$')
    # trace19_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['SRI LANKA - SRI LANKAN RUPEE/US$'],
    #                                mode='lines', name='LKR/US$')
    trace20_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['SWITZERLAND - FRANC/US$'],
                                   mode='lines', name='CHF/US$')
    # trace21_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['TAIWAN - NEW TAIWAN DOLLAR/US$'],
    #                                mode='lines', name='TWD/US$')
    # trace22_multiline = go.Scatter(x=filtered_df['Date'], y=multiline_df['THAILAND - BAHT/US$'],
    #                                mode='lines', name='THB/US$')

    data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline, trace4_multiline,
                      trace5_multiline, trace6_multiline, trace7_multiline, trace8_multiline,
                      trace11_multiline, trace12_multiline,
                      trace13_multiline, trace14_multiline, trace16_multiline,
                      trace17_multiline, trace18_multiline, trace20_multiline, ]

    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_timeframe,
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}


################### Third Graph Callback #############################

@app.callback(Output('graph3', 'figure'),[Input('comparison1', 'value')],[Input('comparison2', 'value')],[Input('button', 'n_clicks')],state=[State('timeframe2', 'value')])
def update_figure3(selected_currency1, selected_currency2, n_clicks, selected_timeframe):
    if ((selected_currency1 is None) or (selected_currency2 is None) or (selected_timeframe is None)):
        raise PreventUpdate
    else:
        filtered_df = multiline_df
        currency1 = selected_currency1
        currency2 = selected_currency2
        if(selected_timeframe != None):
            if(selected_timeframe.isdigit()):
                if (int(selected_timeframe) >= 2000 and int(selected_timeframe) <= 2019):
                    dfTime = new_df2
                    dfTime['Date'] = pd.to_datetime(dfTime['Date'])
                    dfCurrentTime = dfTime[dfTime['Date'].dt.year >= int(selected_timeframe)]
                    filtered_df = dfCurrentTime
        filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        newTrace1_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df[currency1],
                                    mode='lines', name=data_frame_label[currency1])
        newTrace2_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df[currency2], mode='lines',
                                    name=data_frame_label[currency2])
        data_multiline2 = [newTrace1_multiline, newTrace2_multiline]
    return {'data': data_multiline2,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + data_frame_label[selected_currency1] + ' and' + data_frame_label[selected_currency2],
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}


if __name__ == '__main__':
    app.run_server(debug=False)
