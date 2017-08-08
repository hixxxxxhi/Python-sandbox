# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['2010', '2011', '2012', '2013', '2014', '2015', '2016'],
    y=[39.99, 72.29, 125.05, 150.26, 169.22, 231.22, 211.88],
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
               'rgba(204,204,204,1)']),
)

data = [trace0]

layout = go.Layout(
    title='Unit sales in millions',
)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H2(children='Hello Dash'),

    html.Div(children='''
        Unit sales of iPhone worldwide from 2010-2016
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
