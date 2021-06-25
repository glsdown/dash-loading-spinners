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
    "Moon": dls.Moon,
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
    "MutatingDots": dls.MutatingDots,  # FIXME - Appear to go outside the bottom right of the box
    "Oval": dls.Oval,
    "Plane": dls.Plane,  # HACK - Can't change size of it (from source package)
    "PuffAlt": dls.PuffAlt,
    "RevolvingDot": dls.RevolvingDot,  # HACK - Incorrect original implementation
    "Rings": dls.Rings,
    "TailSpin": dls.TailSpin,
    "ThreeDots": dls.ThreeDots,
    "Triangle": dls.Triangle,
    "Watch": dls.Watch,  # TODO - consider renaming as similar to clock?
}

loading_output = html.Div(id="loading-output", style={"height": "100px"})
custom_output = html.Div(
    "Change the SVG code below", id="custom-output", style={"height": "100px"}
)
svg = """<svg width="100%" height="200px" fill="none">
      <path 
        fill="#454599" 
        d="
          M0 67
          C 273,183
            822,-40
            1920.00,106 

          V 359 
          H 0 
          V 67
          Z">
        <animate 
          repeatCount="indefinite" 
          fill="#454599" 
          attributeName="d" 
          dur="5s" 
          values="
            M0 77 
            C 473,283
              822,-40
              1920,116 

            V 359 
            H 0 
            V 67 
            Z; 

            M0 77 
            C 473,-40
              1222,283
              1920,136 

            V 359 
            H 0 
            V 67 
            Z; 

            M0 77 
            C 973,260
              1722,-53
              1920,120 

            V 359 
            H 0 
            V 67 
            Z; 

            M0 77 
            C 473,283
              822,-40
              1920,116 

            V 359 
            H 0 
            V 67 
            Z
            ">
        </animate>
      </path>
    </svg>"""


def getSpinnerBox(title, spinner):
    return dbc.Col(
        html.Div(
            [html.Div(title), spinner(fullscreen=False)],
            className="d-flex flex-column align-items-center justify-content-center border border-primary rounded h-100",
        ),
        className="col-md-3",
        style={"height": "150px"},
    )


allSpinners = [getSpinnerBox(t, s) for t, s in spinner_options.items() if s is not None]


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
        html.Div(
            [
                dbc.Row(
                    allSpinners[i : i + 4],
                    className="m-2",
                )
                for i in range(0, len(allSpinners) - 3, 4)
            ]
        ),
        html.Div(
            dls.Custom(
                custom_output,
                id="custom-loader",
                fullscreen=False,
                fullscreenClassName="bg-light",
                svg=svg,
            ),
            style={"height": "200px"},
            className="container d-flex justify-content-center align-items-center border border-primary rounded my-2",
        ),
        html.Div(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Textarea(
                            id="svg-text", value=svg, style={"height": "200px"}
                        ),
                        className="col-md-9",
                    ),
                    dbc.Col(
                        dbc.Button(
                            "View",
                            id="custom-button",
                            className="btn-success",
                            n_clicks=0,
                        ),
                        className="col-md-3",
                    ),
                ],
            ),
        ),
    ],
)


@app.callback(Output("custom-loader", "svg"), [Input("svg-text", "value")])
def change_custom(value):
    return value


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
    Output("custom-output", "children"),
    [Input("custom-button", "n_clicks")],
)
def load_output(n):

    if n:
        time.sleep(100)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"


@app.callback(
    Output("loading-output", "children"),
    [Input("loading-button", "n_clicks")],
)
def load_output(n):

    if n:
        time.sleep(100)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"


if __name__ == "__main__":
    app.run_server(debug=True)
