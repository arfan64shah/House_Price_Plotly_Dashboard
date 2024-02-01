# import required libraries
import dash
from dash import dcc
import dash_html_components as html

# initialize the app
app = dash.Dash()


# build a layout
app.layout = html.Div([
    html.H1("Dushanbe House Price Analysis"),
    html.Div("Dashboard contains Price Analysis for Houses in Dushanbe")
])

# start the app and server
if __name__ == '__main__':
    app.run_server()