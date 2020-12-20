import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True, serve_locally=True)
server = app.server