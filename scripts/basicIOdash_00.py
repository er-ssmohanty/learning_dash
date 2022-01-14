import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Enter x: ",
        dcc.Input(id='my-input', value='initial value', type='number')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Div(id='my-output2'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='my-output2', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(x):
    return 'x^2 = {}'.format(x*x),'x^3 = {}'.format(x**3)


if __name__ == '__main__':
    app.run_server(debug=True)