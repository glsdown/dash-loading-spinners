import time

import dash_loading_spinners as dls
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

spinner_options = {
    "--- react-spinners ---": None,
    "Beat": dls.Beat,
    "Bounce": dls.Bounce,
    "Circle": dls.Circle,
    "ClimbingBox": dls.ClimbingBox,
    "Clip": dls.Clip,
    "Clock": dls.Clock,
    "Dot": dls.Dot,
    "Fade": dls.Fade,
    "Grid": dls.Grid,
    "Hash": dls.Hash,
    "Moon": dls.Moon,  # FIXME - Not working as expected (bouncing around)
    "Pacman": dls.Pacman,
    "Propagate": dls.Propagate,
    "Puff": dls.Puff,
    "Pulse": dls.Pulse,
    "Ring": dls.Ring,
    "Rise": dls.Rise,
    "Rotate": dls.Rotate,
    "Scale": dls.Scale,
    "Skew": dls.Skew,
    "Square": dls.Square,
    "Sync": dls.Sync,
    "--- react-loading-spinners ---": None,
    "Audio": dls.Audio,
    "BallTriangle": dls.BallTriangle,
    "Bars": dls.Bars,
    "Circles": dls.Circles,
    "GridAlt": dls.GridAlt,
    "Hearts": dls.Hearts,
    "MutatingDots": dls.MutatingDots,
    "Oval": dls.Oval,
    "Plane": dls.Plane,  # FIXME - Doesn't fit in box
    "PuffAlt": dls.PuffAlt,
    "RevolvingDot": dls.RevolvingDot,  # FIXME - Doesn't fit in box
    "Rings": dls.Rings,
    "TailSpin": dls.TailSpin,
    "ThreeDots": dls.ThreeDots,
    "Triangle": dls.Triangle,
    "Watch": dls.Watch,  # TODO - consider renaming as similar to clock?
}

loading_output = html.Div(id="loading-output", style={"height": "100px"})

app.layout = html.Div(
    [
        html.Div(
            dls.Hash(
                loading_output,
                id="loading-item",
                fullscreen=False,
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
                                        value="Hash",
                                    ),
                                ]
                            ),
                            className="col-md-6",
                        ),
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Checkbox(
                                        checked=False, id="fullscreen", className="mr-2"
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
        fullscreen=False,
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
