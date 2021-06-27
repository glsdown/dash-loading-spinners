# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Custom(Component):
    """A Custom component.
Create a custom spinner from an animated SVG

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- debounce (number; default 0):
    When using the spinner as a loading spinner, add a time delay (in
    ms) to the spinner being removed to prevent flickering.

- fullscreen (boolean; optional):
    Boolean that determines if the loading spinner will be displayed
    full-screen or not.

- fullscreenClassName (string; optional):
    CSS class names to apply to the container when in fullscreen.

- fullscreen_style (dict; optional):
    Defines CSS styles for the container when in fullscreen.

- show_initially (boolean; default True):
    Whether the Spinner should show on app start-up before the loading
    state has been determined. Default True.

- svg (string; default `<svg  width=80  height=80  viewBox="0 0 38 38"  xmlns="http://www.w3.org/2000/svg"  aria-label="Loading">  <defs>    <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">      <stop stopColor="black" stopOpacity="0" offset="0%" />      <stop stopColor="black" stopOpacity=".631" offset="63.146%" />      <stop stopColor="black" offset="100%" />    </linearGradient>  </defs>  <g fill="none" fillRule="evenodd">    <g transform="translate(1 1)">      <path d="M36 18c0-9.94-8.06-18-18-18" id="Oval-2" stroke="black" strokeWidth="2">        <animateTransform          attributeName="transform"          type="rotate"          from="0 18 18"          to="360 18 18"          dur="0.9s"          repeatCount="indefinite"        />      </path>      <circle fill="#fff" cx="36" cy="18" r=1>        <animateTransform          attributeName="transform"          type="rotate"          from="0 18 18"          to="360 18 18"          dur="0.9s"          repeatCount="indefinite"        />      </circle>    </g>  </g></svg>`):
    The SVG code to include as the spinner, including required
    animations.

- width (number; default 80):
    The width of the resultant SVG (in px)  This helps to identify how
    big the covering div should be."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, fullscreen_style=Component.UNDEFINED, fullscreenClassName=Component.UNDEFINED, svg=Component.UNDEFINED, width=Component.UNDEFINED, fullscreen=Component.UNDEFINED, debounce=Component.UNDEFINED, show_initially=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'svg', 'width']
        self._type = 'Custom'
        self._namespace = 'dash_loading_spinners'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'svg', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Custom, self).__init__(children=children, **args)
