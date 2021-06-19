import time

import dash_loading_spinners as dls
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

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
            # FIXME: Has odd margins/no padding when not in fullscreen mode
            dls.Loader(
                html.Div(id="loading-output"),
                id="loader",
                fullscreen=True,
                color="#ff0000",
                size=100,  # TODO this isn't relevant for all...
            )
        ),
    ]
)

# FIXME: flashes briefly on load
@app.callback(Output("loader", "type"), [Input("loader-style", "value")])
def change_style(style):
    return style


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
