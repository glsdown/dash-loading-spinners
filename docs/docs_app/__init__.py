import re

import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from docs_app.app import app
from docs_app.component import components
from docs_app.custom import layout as custom_layout
from docs_app.examples import layout as examples_layout
from docs_app.main import layout as main_layout
from docs_app.not_found import layout as not_found_layout

app.title = "Dash Loading Spinners"

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Examples", href="/examples", active="partial"),
                dbc.NavLink("Custom", href="/custom", active="exact"),
                dbc.NavLink(
                    ["Github", html.I(className="fab fa-github ml-1")],
                    href="https://github.com/glsdown/dash-loading-spinners",
                ),
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
    elif pathname == "/custom":
        return custom_layout
    return not_found_layout
