import re

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from component import components
from custom import layout as custom_layout
from dash.dependencies import Input, Output
from helpers import app
from main import layout as main_layout
from not_found import layout as not_found_layout

from examples import layout as examples_layout

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Examples", href="/examples", active="partial"),
                dbc.NavLink("Customise", href="/customise", active="exact"),
            ],
            brand="Dash Loading Spinners",
        ),
        dbc.Container(id="content", className="py-3"),
    ],
    className="dash-bootstrap",
)


@app.callback(Output("content", "children"), [Input("url", "pathname")])
def change_page(pathname):
    if pathname == "/":
        return main_layout
    elif pathname == "/examples":
        return examples_layout
    elif m := re.match("/examples/details/([a-zA-Z0-9]*)", pathname):
        try:
            return components[m.group(1)]
        except KeyError:
            return not_found_layout
    elif pathname == "/customise":
        return custom_layout
    return not_found_layout


if __name__ == "__main__":
    app.run_server(debug=True)
