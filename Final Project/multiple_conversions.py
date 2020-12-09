import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from html import unescape
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['bootstrap.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/ForeignExchange.csv')

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

# Global Variables
from_conversion_symbol = 'USD'
to_conversion_symbol = 'USD'
amount_value = 0.0
converted_value = 0.0
message = ""

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

    html.H6('Convert from:', style={'color': '#666'}),
    dcc.Dropdown(
        id='convert_from-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_from-output-container'),

    html.H6('Convert to:', style={'color': '#666'}),
    dcc.Dropdown(
        id='convert_to-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_to-output-container'),

    html.H6('Amount', style={'color': '#666'}),
    dcc.Input(
        id='num-amount',
        type='number',
        debounce=False,
        placeholder=0.00,
    ),

    html.H4(id='message_container'),
    html.Hr(),

    html.H6('All Currencies:', style={'color': '#666'}),
    html.Table([
        html.Tr([html.Td(html.H6('Currency')), html.Td(html.H6('Symbols')), html.Td(html.H6(' ')), html.Td(html.H6('Value'))]),
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
        html.Tr([html.Td('New Zealand Dollar'), html.Td(['NZD', ]), html.Td('NZ' + unescape('&#36;')), html.Td(id='nzd')]),
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
])


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
        return np.round(x / conversion_dict[from_conversion_symbol] * df_aud, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_brl, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_cad, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_cny, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_dkk, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_eur, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_hkd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_inr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_jpy, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_myr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_mxn, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_nzd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_nok, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_sgd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_zar, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_krw, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_lkr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_sek, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_chf, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_twd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_thb, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_gbp, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_usd, 2),

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
    return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2)), amount_value]


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
    return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2))]

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
            np.round(amount_value / conversion_dict[from_conversion_symbol] * conversion_dict[to_conversion_symbol], 2),
            long_name_dict[to_conversion_symbol])] # to_conversion_symbol)]
        return message



if __name__ == '__main__':
    app.run_server(debug=True)
