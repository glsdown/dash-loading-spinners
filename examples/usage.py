import time

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_loading_spinners as dls
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.UNITED])

spinner_options = {
    # Dots
    "Beat": dls.Beat,
    "ThreeDots": dls.ThreeDots,
    "Pulse": dls.Pulse,
    "Ellipsis": dls.Ellipsis,
    "Rotate": dls.Rotate,
    "Sync": dls.Sync,
    "Propagate": dls.Propagate,
    "Rise": dls.Rise,
    "Dot": dls.Dot,
    "MutatingDots": dls.MutatingDots,
    # Circles
    "Tunnel": dls.Tunnel,
    "Puff": dls.Puff,
    "Target": dls.Target,
    "Rings": dls.Rings,
    "Ripple": dls.Ripple,
    # Grid
    "Grid": dls.Grid,
    "GridFade": dls.GridFade,
    "Circles": dls.Circles,
    # Circle
    "Oval": dls.Oval,
    "RevolvingDot": dls.RevolvingDot,
    "Moon": dls.Moon,
    "TailSpin": dls.TailSpin,
    "Clip": dls.Clip,
    "DualRing": dls.DualRing,
    "RingChase": dls.RingChase,
    "Roller": dls.Roller,
    "Ring": dls.Ring,
    "Bounce": dls.Bounce,
    "SpinningDisc": dls.SpinningDisc,
    "Hourglass": dls.Hourglass,
    # Square
    "Square": dls.Square,
    # Lines
    "Audio": dls.Audio,
    "Scale": dls.Scale,
    "Bars": dls.Bars,
    "Wave": dls.Wave,
    # Triangle
    "BallTriangle": dls.BallTriangle,
    "Triangle": dls.Triangle,
    "Skew": dls.Skew,
    # Special
    "Hash": dls.Hash,
    "Fade": dls.Fade,
    "Clock": dls.Clock,
    "Pacman": dls.Pacman,
    "Hearts": dls.Hearts,
    "ClimbingBox": dls.ClimbingBox,
}

loading_output = html.Div(id="loading-output", style={"height": "100px"})
svg = """<svg
    height="70"
    width="100"
    viewBox="0 0 100% 100%"
    xmlns="http://www.w3.org/2000/svg"
>
    <rect width="100%" height="100%">
        <animate
            attributeName="rx"
            values="0;50;0"
            dur="5s"
            repeatCount="indefinite"
        />
    </rect>
    <circle r="40%" cx="50%" cy="50%" fill="#ffffff">
    </circle>
    <circle r="20%" cx="50%" cy="50%" fill="#000000">
        <animate
            attributeName="r"
            values="20%;40%;20%"
            dur="5s"
            repeatCount="indefinite"
        />
    </circle>
</svg>"""


def getSpinnerBox(title, spinner):
    return dbc.Col(
        html.Div(
            [html.Div(title), spinner(fullscreen=False)],
            className="d-flex flex-column align-items-center "
            "justify-content-center border border-primary rounded h-100",
        ),
        className="col-md-3",
        style={"height": "150px"},
    )


allSpinners = [
    getSpinnerBox(t, s) for t, s in spinner_options.items() if s is not None
]


app.layout = html.Div(
    [
        html.Div("Loading spinners.", className="h1"),
        html.Div(
            "Loading spinners can be used whilst a dash component is loading.",
            className="p",
        ),
        html.Div(
            dls.Hash(
                loading_output,
                id="loading-item",
                fullscreen=False,
                fullscreenClassName="bg-light",
            ),
            id="loader",
            className="container d-flex justify-content-center"
            " align-items-center border border-primary rounded my-2",
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Checkbox(
                                        checked=False,
                                        id="fullscreen",
                                        className="mr-2",
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
        html.Div("All loading spinners.", className="h1"),
        html.Div(
            [
                dbc.Row(
                    allSpinners[i : min(i + 4, len(allSpinners))],
                    className="m-2",
                )
                for i in range(0, len(allSpinners), 4)
            ]
        ),
        html.Div("Custom loading spinners.", className="h1"),
        html.Div(
            "If you have animated SVG code, you can use this as a "
            "custom spinner.",
            className="p",
        ),
        html.Div(
            dls.Custom(
                id="custom-loader",
                fullscreen=False,
                fullscreenClassName="bg-light",
                svg=svg,
            ),
            style={"height": "200px"},
            className="container d-flex justify-content-center "
            "align-items-center border border-primary rounded my-2",
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
                className="mx-2",
            ),
        ),
    ],
)


@app.callback(Output("custom-loader", "svg"), [Input("svg-text", "value")])
def change_custom(value):
    return value


@app.callback(
    Output("loading-item", "fullscreen"), [Input("fullscreen", "checked")]
)
def change_fullscreen(checked):
    return checked


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
    app.run_server(debug=True, port=8088)
