import dash
from dash_loading_spinners import Hash


def test_simple(dash_duo):
    # create an app
    app = dash.Dash()
    app.layout = Hash(color="red", id="spinner")

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#spinner", timeout=2)
