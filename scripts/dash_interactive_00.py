import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

airline_data =  pd.read_csv('../data/airline_data.csv', 
                                                      encoding = "ISO-8859-1",dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash(__name__)
app.layout = html.Div(children=
                    [
                        html.H1("Airline Performance Dashboard",style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),  
                        html.Div([dcc.Input(id="inpyear",value=2010,type='number',style={'height':'50px','font-size':35}),],
                                 style={'font-size': 40}),
                        html.Br(),
                        html.Br(),
                        html.Div([dcc.Graph(id="dergraph")]),
                        html.Div(id='my-output'),
                        html.Div([dcc.Graph(id="thegraph")]),
                    ]
                     )



@app.callback(Output(component_id='dergraph',component_property='figure'),
              Output(component_id='my-output', component_property='children'),
              Output(component_id='thegraph',component_property='figure'),
               Input(component_id='inpyear',component_property='value'))

def get_graph(entered_year):
    df =  airline_data[airline_data['Year']==int(entered_year)]
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    fig = go.Figure(data=go.Line(x=line_data['Month'], y=line_data['ArrDelay'], marker=dict(color='red')))

    fig2 = plt.plot(x=line_data['Month'],y=line_data['ArrDelay'])
    
    return fig,'Output: {}'.format(entered_year),fig2