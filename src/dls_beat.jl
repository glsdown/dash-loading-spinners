# AUTO GENERATED FILE - DO NOT EDIT

export dls_beat

"""
    dls_beat(;kwargs...)
    dls_beat(children::Any;kwargs...)
    dls_beat(children_maker::Function;kwargs...)


A Beat component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component.
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `color` (String; optional): Sets the color of the Spinner. You can also specify any valid CSS color
of your choice (e.g. a hex code, a decimal code or a CSS color name).

If not specified will default to black.
- `debounce` (Real; optional): When using the spinner as a loading spinner, add a time delay (in ms) to
the spinner being removed to prevent flickering.
- `fullscreen` (Bool; optional): Boolean that determines if the loading spinner will be displayed
full-screen or not.
- `fullscreenClassName` (String; optional): CSS class names to apply to the container when in fullscreen.
- `fullscreen_style` (Dict; optional): Defines CSS styles for the container when in fullscreen.
- `margin` (Real; optional): The spinner margin (in px)
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `size` (Real; optional): The spinner size (in px)
- `speedMultiplier` (Real; optional): The relative speed of the spinner
- `spinnerCSS` (Dict; optional): Defines additional CSS styles for the spinner itself. It's based on the
emotion css styles here: https://emotion.sh/docs/introduction
"""
function dls_beat(; kwargs...)
        available_props = Symbol[:children, :id, :color, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :margin, :show_initially, :size, :speedMultiplier, :spinnerCSS]
        wild_props = Symbol[]
        return Component("dls_beat", "Beat", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_beat(children::Any; kwargs...) = dls_beat(;kwargs..., children = children)
dls_beat(children_maker::Function; kwargs...) = dls_beat(children_maker(); kwargs...)

