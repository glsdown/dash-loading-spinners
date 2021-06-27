# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DualRing(Component):
    """A DualRing component.
Two arcs rotating around in a circle opposite each other.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- color (string; default '#000000'):
    Sets the color of the Spinner. You can also specify any valid CSS
    color of your choice (e.g. a hex code, a decimal code or a CSS
    color name).  If not specified will default to black.

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

- thickness (number; default 6):
    The line thickness for the circle.

- width (number; default 60):
    The width of the spinner (in px)."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, fullscreen_style=Component.UNDEFINED, fullscreenClassName=Component.UNDEFINED, color=Component.UNDEFINED, width=Component.UNDEFINED, thickness=Component.UNDEFINED, fullscreen=Component.UNDEFINED, debounce=Component.UNDEFINED, show_initially=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'thickness', 'width']
        self._type = 'DualRing'
        self._namespace = 'dash_loading_spinners'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'thickness', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DualRing, self).__init__(children=children, **args)
