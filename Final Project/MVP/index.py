import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# import pandas as pd
# import numpy as np
# import plotly.graph_objs as go
# from html import unescape
# from dash.exceptions import PreventUpdate

from app import app
from layouts import currency_converter, \
                    high_level_overview, \
                    single_currency_focus, \
                    currency_comparison, \
                    user_instructions

import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return currency_converter
    elif pathname == '/currency_converter':
         return currency_converter
    elif pathname == '/high_level_overview':
         return high_level_overview
    elif pathname == '/single_currency_focus':
         return single_currency_focus
    elif pathname == '/currency_comparison':
         return currency_comparison
    elif pathname == '/user_instructions':
         return user_instructions
    else:
        return '404'



if __name__ == '__main__':
    app.run_server(debug=False)