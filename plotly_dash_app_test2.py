# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go

# Data
trace1 = go.Bar(
    x=[year for year in range(1999, 2017)],
    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
       350, 430, 474, 526, 488, 537, 500, 439],
    name='Product A',
    marker=dict(
        color='rgba(222, 45, 38, 0.9)'
    )
)
trace2 = go.Bar(
    x=[year for year in range(1999, 2017)],
    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
       299, 340, 403, 549, 499],
    name='Product B',
    marker=dict(
        color='rgba(26, 118, 255, 0.9)'
    )
)
data = [trace1, trace2]

# Layout
layout = go.Layout(
    title='Unit sales worldwide 1999-2016',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Unit sales in millions',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

# Dash app
app = dash.Dash()

app.layout = html.Div(children=[
    html.H2(children='Visualization with Dash'),

    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam porttitor non sem posuere malesuada. In vitae vulputate mauris. Sed ac nulla et nisl fringilla luctus vitae vitae quam. Vestibulum facilisis odio at egestas viverra. Suspendisse potenti.
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
