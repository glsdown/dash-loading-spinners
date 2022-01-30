import dash
import dash_loading_spinners as dls
import pytest

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


@pytest.mark.parametrize("spinner_name,spinner", spinner_options.items())
def test_simple(dash_duo, spinner_name, spinner):

    # create an app
    app = dash.Dash()
    app.layout = spinner(id=spinner_name)

    dash_duo.start_server(app)
    dash_duo.wait_for_element(f"#{spinner_name}", timeout=2)
