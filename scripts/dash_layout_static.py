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

#
#
#
#
#

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

fig_anyname = px.bar(df,x="Fruit",y="Amount",color="City",barmode="group")

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
    dcc.Dropdown(options=[
            dict(label='New York City',value='NYC'),
            dict(label='Montreal',value='MTL'),
            dict(label='San Francisco',value='SF')
        ],
        value = 'NYC' #default
    ),
    # Bar graph
    dcc.Graph(id='a_random_name',figure=fig_anyname)

])

#
#
#
#
#

if __name__ == '__main__':
    app.run_server()
