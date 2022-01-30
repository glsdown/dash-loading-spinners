import dash_loading_spinners as dls
from dash import dcc, html

svg = """
<svg
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
  <circle r="40%" cx="50%" cy="50%" fill="#ffffff"></circle>
  <circle r="20%" cx="50%" cy="50%" fill="#000000">
    <animate
      attributeName="r"
      values="20%;40%;20%"
      dur="5s"
      repeatCount="indefinite"
    />
  </circle>
</svg>
"""

markdown = f"""
# Custom Loading Spinners

Making use of the `Custom` spinner allows you to pass in your own animated
SVG code to use as a spinner.

```python
import dash
import dash_loading_spinners as dls
from dash import html

app = dash.Dash()

svg = \"\"\"{svg}\"\"\"
app.layout = html.Div(dls.Custom(svg=svg), style={{"height": "200px"}})

if __name__ == "__main__":
    app.run_server()
```

As with other spinners, you are also able to edit the core attributes:

- **`id`** (*string*; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.
- **`children`** (*a list of or a singular dash component, string or \
  number*; optional):
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
"""

layout = html.Div(
    [
        dcc.Markdown(markdown),
        html.Div(
            dls.Custom(svg=svg,),
            style={"height": "200px"},
            className="container d-flex justify-content-center "
            "align-items-center border border-primary rounded my-2",
        ),
    ]
)
