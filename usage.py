import time

import dash_loading_spinners as dls
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

spinner_options = {
    # "bar",
    "beat": dls.RSBeat,
    "bounce": dls.RSBounce,
    "circle": dls.RSCircle,
    "climbingBox": dls.RSClimbingBox,
    "clip": dls.RSClip,
    "clock": dls.RSClock,
    "dot": dls.RSDot,
    "fade": dls.RSFade,
    "grid": dls.RSGrid,
    "hash": dls.RSHash,
    "moon": dls.RSMoon,
    "pacman": dls.RSPacman,
    "propagate": dls.RSPropagate,
    "puff": dls.RSPuff,
    "pulse": dls.RSPulse,
    "ring": dls.RSRing,
    "rise": dls.RSRise,
    "rotate": dls.RSRotate,
    "scale": dls.RSScale,
    "sync": dls.RSSync,
}

loading_output = html.Div(id="loading-output", style={"height": "100px"})

app.layout = html.Div(
    [
        html.Div(
            dls.RSHash(
                loading_output,
                id="loading-item",
                fullscreen=True,
                fullscreenClassName="bg-light",
            ),
            id="loader",
            className="container d-flex justify-content-center align-items-center border border-primary rounded my-2",
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Label("Loader Style"),
                                    dcc.Dropdown(
                                        id="loader-style",
                                        options=[
                                            {"label": s, "value": s}
                                            for s in spinner_options.keys()
                                        ],
                                        value="hash",
                                    ),
                                ]
                            ),
                            className="col-md-6",
                        ),
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Checkbox(
                                        checked=True, id="fullscreen", className="mr-2"
                                    ),
                                    dbc.Label("Fullscreen?"),
                                ]
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.FormGroup(
                                dbc.Button(
                                    "View",
                                    id="loading-button",
                                    className="btn-success",
                                    n_clicks=0,
                                )
                            ),
                            className="col-md-2",
                        ),
                    ],
                    className="align-items-end",
                )
            ],
            className="container",
        ),
    ]
)


@app.callback(Output("loading-item", "fullscreen"), [Input("fullscreen", "checked")])
def change_fullscreen(checked):
    return checked


@app.callback(Output("loader", "children"), [Input("loader-style", "value")])
def change_loader(value):

    return spinner_options[value](
        loading_output,
        id="loading-item",
        fullscreen=True,
        fullscreenClassName="bg-light",
    )


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
