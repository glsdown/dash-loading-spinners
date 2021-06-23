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
        dbc.Button("View", id="loading-button", n_clicks=0),
        html.Div(
            dls.RSHash(
                loading_output,
                fullscreen=False,
                coverClassName="bg-primary",
            ),
            id="loader",
            className="container d-flex justify-content-center align-items-center border border-primary rounded my-2",
        ),
        # TODO: Fix this
        dbc.FormGroup(
            [
                dbc.Label("Loader Style"),
                dcc.Dropdown(
                    id="loader-style",
                    options=[{"label": s, "value": s} for s in spinner_options.keys()],
                    value="hash",
                ),
            ]
        ),
    ]
)


@app.callback(Output("loader", "children"), [Input("loader-style", "value")])
def change_loader(value):

    return spinner_options[value](
        loading_output,
        fullscreen=True,
        fullscreenClassName="bg-primary",
    )


@app.callback(
    Output("loading-output", "children"),
    [Input("loading-button", "n_clicks")],
)
def load_output(n):

    if n:
        time.sleep(10)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"


if __name__ == "__main__":
    app.run_server(debug=True)
