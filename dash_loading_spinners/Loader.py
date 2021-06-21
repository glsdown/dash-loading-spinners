# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Loader(Component):
    """A Loader component.


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
    Often used with CSS to style elements with common properties.

- fullscreen_style (dict; optional):
    Defines CSS styles for the container when fullscreen=True.

- height (number; optional):
    The spinner height (in px) - only applicable for loaders of type:
    - bar - fade - scale.

- margin (number; optional):
    The spinner margin (in px) - only applicable for loaders of type:
    - beat - dot - fade - hash - moon - pacman - pulse - ring - rise -
    rotate - scale - sync.

- radius (number; optional):
    The spinner radius (in px) - only applicable for loaders of type:
    - fade - scale.

- show_initially (boolean; default True):
    Whether the Spinner should show on app start-up before the loading
    state has been determined. Default True.

- size (number; optional):
    The spinner size (in px) - not applicable for loaders of type: -
    bar - fade - scale.

- speedMultiplier (number; default 1):
    The relative speed of the spinner.

- spinnerCSS (dict; optional):
    Defines additional CSS styles for the spinner itself. It's based
    on the emotion css styles here:
    https://emotion.sh/docs/introduction.

- spinnerClassName (string; optional):
    CSS class names to apply to the container when fullscreen=False.

- spinner_style (dict; optional):
    Defines CSS styles for the container when fullscreen=False.

- type (string; default 'default'):
    The type of spinner. Options are: - bar - beat - bounce - circle -
    climbingBox - clip - clock - dot - fade - grid - hash - moon -
    pacman - propagate - puff - pulse - ring - rise - rotate - scale -
    sync.

- width (number; optional):
    The spinner width (in px) - only applicable for loaders of type: -
    bar - fade - scale."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, fullscreen_style=Component.UNDEFINED, spinner_style=Component.UNDEFINED, fullscreenClassName=Component.UNDEFINED, spinnerClassName=Component.UNDEFINED, color=Component.UNDEFINED, spinnerCSS=Component.UNDEFINED, type=Component.UNDEFINED, speedMultiplier=Component.UNDEFINED, size=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, radius=Component.UNDEFINED, margin=Component.UNDEFINED, fullscreen=Component.UNDEFINED, debounce=Component.UNDEFINED, show_initially=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'margin', 'radius', 'show_initially', 'size', 'speedMultiplier', 'spinnerCSS', 'spinnerClassName', 'spinner_style', 'type', 'width']
        self._type = 'Loader'
        self._namespace = 'dash_loading_spinners'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'margin', 'radius', 'show_initially', 'size', 'speedMultiplier', 'spinnerCSS', 'spinnerClassName', 'spinner_style', 'type', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Loader, self).__init__(children=children, **args)
