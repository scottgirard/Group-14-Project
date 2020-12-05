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
df_kpw = df1['KOREA - WON/US$'].iloc[-1]
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

app.layout = html.Div([
    html.H6('Enter an amount in US currency', style={'color': '#666'}),
    dcc.Input(
        id='num-multi',
        type='number',
        debounce=True,
        placeholder=0.00,
        value=1.00
    ),

    html.Table([
        html.Tr([html.Td(html.H6('Currency')), html.Td(html.H6('Symbols')), html.Td(html.H6(' ')), html.Td(html.H6('Value'))]),
        html.Tr([html.Td('Australia Dollar'), html.Td('AUD'), html.Td('A' + unescape('&#36;')), html.Td(id='aud')]),
        html.Tr([html.Td('Brazil Real'), html.Td(['BRL', ]), html.Td('R'+ unescape('&#36;')), html.Td(id='brl')]),
        html.Tr([html.Td('Canada Dollar'), html.Td(['CAD', ]), html.Td('C'+ unescape('&#36;')), html.Td(id='cad')]),
        html.Tr([html.Td('Switzerland Franc'), html.Td(['CHF', ]), html.Td('fr'), html.Td(id='chf')]),
        html.Tr([html.Td('China Yuan'), html.Td(['CNY', ]), html.Td(unescape('&#20803;')), html.Td(id='cny')]),
        html.Tr([html.Td('Denmark Krone'), html.Td(['DKK', ]), html.Td('kr'), html.Td(id='dkk')]),
        html.Tr([html.Td('Euro Members'), html.Td(['EUR', ]), html.Td(unescape('&#8364;')), html.Td(id='eur')]),
        html.Tr([html.Td('United Kingdom Pound'), html.Td(['GBP', ]), html.Td(unescape('&#163;')), html.Td(id='gbp')]),
        html.Tr([html.Td('Hong Kong Dollar'), html.Td(['HKD', ]), html.Td('HK' + unescape('&#36;')), html.Td(id='hkd')]),
        html.Tr([html.Td('India Rupee'), html.Td(['INR', ]), html.Td(unescape('&#8377;')), html.Td(id='inr')]),
        html.Tr([html.Td('Japan Yen'), html.Td(['JPY', ]), html.Td(unescape('&#165;')), html.Td(id='jpy')]),
        html.Tr([html.Td('South Korea Won'), html.Td(['KRW', ]), html.Td(unescape('&#8361;')), html.Td(id='kpw')]),
        html.Tr([html.Td('Sri Lanka Rupee'), html.Td(['LKR', ]), html.Td('Rs'), html.Td(id='lkr')]),
        html.Tr([html.Td('Mexico Peso'), html.Td(['MXN', ]), html.Td('Mex' + unescape('&#36;')), html.Td(id='mxn')]),
        html.Tr([html.Td('Malaysia Ringgit'), html.Td(['MYR', ]), html.Td('RM'), html.Td(id='myr')]),
        html.Tr([html.Td('Norway Krone'), html.Td(['NOK', ]), html.Td('kr'), html.Td(id='nok')]),
        html.Tr([html.Td('New Zealand Dollar'), html.Td(['NZD', ]), html.Td('NZ' + unescape('&#36;')), html.Td(id='nzd')]),
        html.Tr([html.Td('Sweden Krona'), html.Td(['SEK', ]), html.Td('kr'), html.Td(id='sek')]),
        html.Tr([html.Td('Singapore Dollar'), html.Td(['SGD', ]), html.Td('S' + unescape('&#36;')), html.Td(id='sgd')]),
        html.Tr([html.Td('Thailand Baht'), html.Td(['THB', ]), html.Td(unescape('&#3647;')), html.Td(id='thb')]),
        html.Tr([html.Td('Taiwan New Dollar'), html.Td(['TWD', ]), html.Td('NT'+unescape('&#36;')), html.Td(id='twd')]),
        html.Tr([html.Td('South Africa Rand'), html.Td(['ZAR', ]), html.Td('R'), html.Td(id='zar')]),
    ]),
])


@app.callback(
    Output('aud', 'children'),
    Output('eur', 'children'),
    Output('nzd', 'children'),
    Output('gbp', 'children'),
    Output('brl', 'children'),
    Output('cad', 'children'),
    Output('cny', 'children'),
    Output('hkd', 'children'),
    Output('inr', 'children'),
    Output('kpw', 'children'),
    Output('mxn', 'children'),
    Output('zar', 'children'),
    Output('sgd', 'children'),
    Output('dkk', 'children'),
    Output('jpy', 'children'),
    Output('myr', 'children'),
    Output('nok', 'children'),
    Output('sek', 'children'),
    Output('lkr', 'children'),
    Output('chf', 'children'),
    Output('twd', 'children'),
    Output('thb', 'children'),

    Input('num-multi', 'value'))

def callback_a(x):
    if x is None:
        raise PreventUpdate
    else:
        return np.round(x * df_aud, 2), \
           np.round(x * df_eur, 2), \
           np.round(x * df_nzd, 2), \
           np.round(x * df_gbp, 2), \
           np.round(x * df_brl, 2), \
           np.round(x * df_cad, 2), \
           np.round(x * df_cny, 2), \
           np.round(x * df_hkd, 2), \
           np.round(x * df_inr, 2), \
           np.round(x * df_kpw, 2), \
           np.round(x * df_mxn, 2), \
           np.round(x * df_zar, 2), \
           np.round(x * df_sgd, 2), \
           np.round(x * df_dkk, 2), \
           np.round(x * df_jpy, 2), \
           np.round(x * df_myr, 2), \
           np.round(x * df_nok, 2), \
           np.round(x * df_sek, 2), \
           np.round(x * df_lkr, 2), \
           np.round(x * df_chf, 2), \
           np.round(x * df_twd, 2), \
           np.round(x * df_thb, 2)


if __name__ == '__main__':
    app.run_server(debug=True)
