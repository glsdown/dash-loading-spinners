from dash.dependencies import Input, Output
from dash_html_components.Content import Content
import dash_loading_spinners as dls
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import re

from main import layout as main_layout
from examples import layout as examples_layout
from component import layout as component_layout
from custom import layout as custom_layout
from not_found import layout as not_found_layout
from helpers import app


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
    ]
)


@app.callback(Output("content", "children"), [Input("url", "pathname")])
def change_page(pathname):
    if pathname == "/":
        return main_layout
    elif pathname == "/examples":
        return examples_layout
    elif m := re.match("/examples/details/([a-zA-Z0-9]*)", pathname):
        return component_layout(m.group(1))
    elif pathname == "/customise":
        return custom_layout
    return not_found_layout


if __name__ == "__main__":
    app.run_server(debug=True)
