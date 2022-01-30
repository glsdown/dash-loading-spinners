# Component Page:
# - Demo of each component in a grid
# - Potentially include ability to change props on the page?

import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
from dash import Input, Output, dcc, html

from docs_app.app import app

spinner_options = {
    "Dots": {
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
    },
    "Grids": {
        "Grid": dls.Grid,
        "GridFade": dls.GridFade,
        "Circles": dls.Circles,
    },
    "Concentric Rings": {
        "Puff": dls.Puff,
        "Target": dls.Target,
        "Rings": dls.Rings,
        "Ripple": dls.Ripple,
    },
    "Spinning Rings": {
        "Oval": dls.Oval,
        "RevolvingDot": dls.RevolvingDot,
        "Moon": dls.Moon,
        "TailSpin": dls.TailSpin,
        "Clip": dls.Clip,
        "DualRing": dls.DualRing,
        "RingChase": dls.RingChase,
        "Roller": dls.Roller,
        "Ring": dls.Ring,
        "Tunnel": dls.Tunnel,
        "Fade": dls.Fade,
    },
    "Solid Shapes": {
        "Hourglass": dls.Hourglass,
        "SpinningDisc": dls.SpinningDisc,
        "Bounce": dls.Bounce,
        "Square": dls.Square,
        "Skew": dls.Skew,
    },
    "Bars": {
        "Audio": dls.Audio,
        "Scale": dls.Scale,
        "Bars": dls.Bars,
        "Wave": dls.Wave,
    },
    "Triangles": {
        "BallTriangle": dls.BallTriangle,
        "Triangle": dls.Triangle,
    },
    "Special": {
        "Hash": dls.Hash,
        "Clock": dls.Clock,
        "Pacman": dls.Pacman,
        "Hearts": dls.Hearts,
        "ClimbingBox": dls.ClimbingBox,
    },
}


def getSpinnerBox(title, spinner):
    return dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    dcc.Link(title, href=f"/examples/details/{title}")
                ),
                dbc.CardBody(spinner(fullscreen=False), className="py-auto"),
            ],
            style={"height": "200px"},
        ),
        # xs=12,
        md=3,
        className="mb-3",
    )


def getSpinnerGroup(title, group):
    group_spinners = [getSpinnerBox(t, s) for t, s in group.items()]
    return html.Div(
        [
            html.Div(title, className="h2 text-secondary"),
            dbc.Row(group_spinners),
            html.Hr(),
        ]
    )


def getSpinnerSorted():
    spinners_sorted = {}
    for _, v in spinner_options.items():
        spinners_sorted.update(v)
    return spinners_sorted


spinners_sorted = getSpinnerSorted()


allSpinners = [getSpinnerGroup(t, g) for t, g in spinner_options.items()]
allSpinnersSorted = dbc.Row(
    [getSpinnerBox(t, spinners_sorted[t]) for t in sorted(spinners_sorted)]
)


layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    "All loading spinners.", className="h1 col-12 col-sm"
                ),
                html.Div(
                    [
                        html.Div("View Grouped", className="me-2"),
                        dbc.Switch(
                            id="alpha-switch",
                            label="View Alphabetical",
                            value=False,
                        ),
                    ],
                    className="d-flex  col-12 col-sm-auto",
                ),
            ],
            className="row justify-content-between align-items-end",
        ),
        html.Div(html.P("Click any spinner to view detailed usage.")),
        html.Hr(),
        html.Div(allSpinners, id="spinner-display"),
    ],
)


@app.callback(
    Output("spinner-display", "children"), [Input("alpha-switch", "value")]
)
def change_spinner_sort(value):
    if value:
        return allSpinnersSorted
    return allSpinners
