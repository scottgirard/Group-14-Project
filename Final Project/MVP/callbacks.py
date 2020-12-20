from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
import pandas as pd
from app import app
from layouts import multiline_df, \
                    data_frame_label, \
                    new_df2, dfCurrentYear, \
                    dfCurrentDecade, \
                    amount_value, \
                    long_name_dict, \
                    conversion_dict, \
                    df_aud, df_brl, df_cad, df_cny, df_dkk, df_eur, df_hkd, df_inr, \
                    df_jpy, df_myr, df_mxn, df_nzd, df_nok, df_sgd, df_zar, df_krw, \
                    df_lkr, df_sek, df_chf, df_twd, df_thb, df_gbp, df_usd


###################### Currency Converter Callback #######################

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
        message = ['{} {} = {} {}'.format(amount_value,
            long_name_dict[from_conversion_symbol], # from_conversion_symbol,
            round(amount_value / conversion_dict[from_conversion_symbol] * conversion_dict[to_conversion_symbol], 2),
            long_name_dict[to_conversion_symbol])] # to_conversion_symbol)]
        return message

######################### High Level Overview Callback ##############################

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

    trace1_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'],
                   mode='lines',
                   name='AUD/US$')
    trace2_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['EURO AREA - EURO/US$'],
                   mode='lines',
                   name='EUR/US$')
    trace3_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                   mode='lines',
                   name='NZD/US$')
    trace4_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                   mode='lines',
                   name='GBP/US$')
    trace5_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['BRAZIL - REAL/US$'],
                   mode='lines',
                   name='BRL/US$')
    trace6_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['CANADA - CANADIAN DOLLAR/US$'],
                   mode='lines',
                   name='CAD/US$')
    trace7_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['CHINA - YUAN/US$'],
                   mode='lines',
                   name='CNY/US$')
    trace8_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['HONG KONG - HONG KONG DOLLAR/US$'],
                   mode='lines',
                   name='HKD/US$')
    # trace9_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['INDIA - INDIAN RUPEE/US$'],
    #              mode='lines',
    #              name='INR/US$')
    # trace10_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['KOREA - WON/US$'],
    #              mode='lines',
    #              name='KRW/US$')
    trace11_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['MEXICO - MEXICAN PESO/US$'],
                   mode='lines',
                   name='MXN/US$')
    trace12_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['SOUTH AFRICA - RAND/US$'],
                   mode='lines',
                   name='ZAR/US$')
    trace13_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['SINGAPORE - SINGAPORE DOLLAR/US$'],
                   mode='lines',
                   name='SGD/US$')
    trace14_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['DENMARK - DANISH KRONE/US$'],
                   mode='lines',
                   name='DKK/US$')
    # trace15_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['JAPAN - YEN/US$'],
    #              mode='lines',
    #              name='JPY/US$')
    trace16_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['MALAYSIA - RINGGIT/US$'],
                   mode='lines',
                   name='MYR/US$')
    trace17_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['NORWAY - NORWEGIAN KRONE/US$'],
                   mode='lines',
                   name='NOK/US$')
    trace18_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['SWEDEN - KRONA/US$'],
                   mode='lines',
                   name='SEK/US$')
    # trace19_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['SRI LANKA - SRI LANKAN RUPEE/US$'],
    #              mode='lines',
    #              name='LKR/US$')
    trace20_multiline = \
        go.Scatter(x=filtered_df['Date'],
                   y=multiline_df['SWITZERLAND - FRANC/US$'],
                   mode='lines',
                   name='CHF/US$')
    # trace21_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['TAIWAN - NEW TAIWAN DOLLAR/US$'],
    #              mode='lines',
    #              name='TWD/US$')
    # trace22_multiline = \
    #   go.Scatter(x=filtered_df['Date'],
    #              y=multiline_df['THAILAND - BAHT/US$'],
    #              mode='lines',
    #              name='THB/US$')

    data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline, trace4_multiline,
                      trace5_multiline, trace6_multiline, trace7_multiline, trace8_multiline,
                      trace11_multiline, trace12_multiline,
                      trace13_multiline, trace14_multiline, trace16_multiline,
                      trace17_multiline, trace18_multiline, trace20_multiline, ]

    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_timeframe,
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}

######################### Currency Focus Callback ##############################

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

################### Currency Comparison Callback #############################

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
