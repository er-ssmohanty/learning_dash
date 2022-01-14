'''
!pip install dash
!pip install pandas
'''

import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table as dt

#
#
#
#
#

app = dash.Dash()
app.layout = html.Div(children = [
    html.H1(
        children = 'Dashboard',
        style = dict(textAlign='center')
        ),
    # Create dropdown
    dcc.Dropdown(id='dd1',options=[
            dict(label='New York City',value='NYC'),
            dict(label='Montreal',value='MTL'),
            dict(label='All',value='ALL'),
            dict(label='San Francisco',value='SF')
        ],
        value = 'NYC' #default
    ),
    # Bar graph
    #dcc.Graph(id='a_random_name')
    #2#html.Td(id='my-output'),
    dt.DataTable(id='my-output',columns=[{'name': 'Fruit', 'id': 'Fruit'},
     {'name': 'Amount', 'id': 'Amount'}]),
    dt.Table(id="my-output")
    #columns=[{"name": i, "id": i} for i in df.columns],
    #data=df.to_dict('records'),
    #'''
])

#
#
#
#
#

@app.callback(Output(component_id='my-output',component_property='data'),
            Input(component_id='dd1',component_property='value'))

def randomly_named(citycode):
    df = pd.DataFrame({
     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
     "Amount": [4, 1, 2, 2, 4, 5],
     "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]})

    if citycode=='ALL':
        pass
    else:
        df=df[df['City']=='SF']
    data2 = df[['Fruit','Amount']].to_dict(orient='records')
    return data.to_dict(orient='records')

#
#
#
#
#

if __name__ == '__main__':
    app.run_server()


"""
I tried so hard and got so far,
in the end, it doesn't even matter.
"""
