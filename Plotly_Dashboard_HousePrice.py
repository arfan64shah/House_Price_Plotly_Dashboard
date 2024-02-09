# import required libraries
import dash
from dash import dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# load and read dataset
dataset = pd.read_csv('dataset.csv')

# initialize the app
app = dash.Dash()


# build a layout
app.layout = html.Div([
    html.H1("Dushanbe House Price Analysis", style={'textAlign': 'center', 'backgroundColor': '#f8c471', 
                                                    'paddingTop': '10px', 'marginTop':'0px', 'width':'100%', 
                                                    'height':'60px'}),
    #html.Div("Dashboard contains Price Analysis for Houses in Dushanbe"),
    html.Div([
        dcc.Graph(
            id = 'scatter-graph',
            figure = {
                               
                'data': [                    
                    go.Scatter(x = dataset['number_of_rooms'], y = dataset['price'], marker = dict(color = 'green'), name = 'No of Rooms VS Price')
            ],
                'layout': go.Layout(
                    title = 'Rooms VS Price',
                    xaxis = {'title' : 'No of Rooms'},
                    yaxis = {'title' : 'Price'}
            )   }
            )
    ],
        style={'width': '49%', 'display': 'inline-block'}
        ),
    # plot a bar graph
    html.Div([
        dcc.Graph(
            id = 'histogram',
            figure = {
                'data': [
                    go.Histogram(x = dataset['number_of_rooms'], nbinsx = 6)
                ],
                'layout': go.Layout(
                    title = "Number of Rooms",
                    bargap = 0.2
                )
            }
        )
    ],
             style = {'width': '49%', 'display' : 'inline_block'}
             )
])

# start the app and server
if __name__ == '__main__':
    app.run_server()