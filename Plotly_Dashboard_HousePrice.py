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
    html.H1("Dushanbe House Price Analysis"),
    html.Div("Dashboard contains Price Analysis for Houses in Dushanbe"),
    
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
            )
            
        }
    ),
    # plot a bar graph
    dcc.Graph(
        id = 'bar-graph',
        figure = {
            'data': [
                go.Line(x = dataset['number_of_rooms'], y = dataset['price'])
            ]
        }
    )
    
])

# start the app and server
if __name__ == '__main__':
    app.run_server()