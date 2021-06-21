import time

import dash_loading_spinners as dls
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

spinner_options = [
    "bar",
    "beat",
    "bounce",
    "circle",
    "climbingBox",
    "clip",
    "clock",
    "dot",
    "fade",
    "grid",
    "hash",
    "moon",
    "pacman",
    "propagate",
    "puff",
    "pulse",
    "ring",
    "rise",
    "rotate",
    "scale",
    "sync",
]

app.layout = html.Div(
    [
        dbc.Button("View", id="loading-button", n_clicks=0),
        html.Div(
            dls.Loader(
                html.Div(id="loading-output", style={"height": "100px"}),
                fullscreen=False,
                spinnerClassName="bg-primary",
                color="#ff0000",
                width=100,
            )
        ),
        dbc.FormGroup(
            [
                dbc.Label("Loader Style"),
                dcc.Dropdown(
                    id="loader-style",
                    options=[{"label": s, "value": s} for s in spinner_options],
                    value="hash",
                ),
            ]
        ),
        html.Div(
            dls.Loader(
                id="loader",
                fullscreen=False,
                spinnerClassName="bg-warning",
                color="#00ff00",
                spinnerCSS={"border-color": "red"},
            )
        ),
    ]
)

# FIXME: flashes briefly on load
@app.callback(Output("loader", "type"), [Input("loader-style", "value")])
def change_style(spinner_style):
    return spinner_style


@app.callback(
    Output("loading-output", "children"),
    [Input("loading-button", "n_clicks")],
)
def load_output(n):

    if n:
        time.sleep(3)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"


if __name__ == "__main__":
    app.run_server(debug=True)
