# Dash Loading Spinners

[![Tests](https://github.com/glsdown/dash-loading-spinners/actions/workflows/test.yml/badge.svg)](https://github.com/glsdown/dash-loading-spinners/actions/workflows/test.yml)
![PyPI](https://img.shields.io/pypi/v/dash-loading-spinners)
![PyPI - License](https://img.shields.io/pypi/l/dash-loading-spinners)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dash-loading-spinners)
[![Downloads](https://static.pepy.tech/personalized-badge/dash-loading-spinners?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/dash-loading-spinners)

This library is designed for use with [Plotly Dash](https://plotly.com). The components have all been
designed to provide functionality similar to Dash's core 
[`Loading` component](https://dash.plotly.com/dash-core-components/loading),
and will display a loading spinner whilst the underlying children are re-rendering.

The spinners in it have been adapted for use from a number of other existing
libraries:

- [react-spinners](https://github.com/davidhu2000/react-spinners)
- [react-loader-spinner](https://github.com/mhnpd/react-loader-spinner)
- [react-css-spinners](https://github.com/alex996/react-css-spinners)

The majority of spinner names have been retained from the originals, but some have 
been amended where there were name clashes.

More details on the components and usage can be found in our [documentation](https://dash-loading-spinners.sproodlebuzz.co.uk/).

---
## Installation

Dash Loading Spinners is available through 
[PyPI](https://pypi.org/project/dash-loading-spinners/), and can be installed with pip:

```bash
pip install dash-loading-spinners
```

---
## Basic Usage

Once installed, you can make use of the components (in their most basic sense) as follows:

```python
import dash
import dash_loading_spinners as dls

app = dash.Dash()

app.layout = dls.Hash()

if __name__ == "__main__":
    app.run_server()
```

There are a number of attributes which are common across all spinners. These are:

- **`id`** (*string*; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app. 
- **`children`** (*a list of or a singular dash component, string or number*; optional):
    The children of this component.
- **`show_initially`** (*boolean*; default `True`):
    Whether the Spinner should show on app start-up before the loading
    state has been determined. Default True.
- **`debounce`** (*number*; default `0`):
    When using the spinner as a loading spinner, add a time delay (in
    ms) to the spinner being removed to prevent flickering.
- **`fullscreen`** (*boolean*; optional):
    Boolean that determines if the loading spinner will be displayed
    full-screen or not.
- **`fullscreenClassName`** (*string*; optional):
    CSS class names to apply to the container when in fullscreen.
- **`fullscreen_style`** (*dict*; optional):
    Defines CSS styles for the container when in fullscreen.

Many spinners additional have properties that can be customised, including colour and size. You 
can find these on the individual [component](https://dash-loading-spinners.sproodlebuzz.co.uk/examples) pages. 

Realistically, as part of an application, you will be using them alongside other components and 
callbacks. Here is an example of what this might look like:

_Note: 
[`dash-bootstrap-components`](https://github.com/facultyai/dash-bootstrap-components) 
isn't necessary for `dash-loading-spinners` to work, but has been included
to improve the layout._

```python
# app.py
import dash
import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
from dash import dcc, html, Input, Output

from helpers import get_new_graph

app = dash.Dash(external_stylesheets=[dbc.themes.UNITED])

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dbc.Button(
                            "Simulate slow loading component",
                            id="loading-button",
                            className="btn-success",
                            n_clicks=0,
                        )
                    ),
                    md=3,
                ),
                dbc.Col(
                    dls.Hash(
                        dcc.Graph(id="loading-output",),
                        color="#435278",
                        speed_multiplier=2,
                        size=100,
                    ),
                    md=9,
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("loading-output", "figure"), [Input("loading-button", "n_clicks")],
)
def load_output(n):
    # See note below
    return get_new_graph(n)

if __name__ == "__main__":
    app.run_server()

```

The function `get_new_graph` in this example is deliberately ambiguous, as it simply acts as a placeholder for any slow-loading component. For completeness, if you wish to use a similar example to the one shown above, you can use the following function:

```python
# helpers.py
import numpy as np
import plotly.graph_objects as go
import time

def get_new_graph(n):
    if n:
        # Simulate slow-loading component
        time.sleep(2)
    # Generate a random scatter plot
    n = (n + 1) * 10
    return go.Figure(
        data=go.Scatter(
            y=np.random.randn(n) * 100,
            mode="markers",
            marker=dict(
                size=16,
                color=np.random.randn(n) * 100,
                colorscale="blues",
                showscale=True,
            ),
        ),
        layout=go.Layout(title="This graph takes ages to re-load"),
    )
```
