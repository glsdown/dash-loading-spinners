# AUTO GENERATED FILE - DO NOT EDIT

export dls_square

"""
    dls_square(;kwargs...)
    dls_square(children::Any;kwargs...)
    dls_square(children_maker::Function;kwargs...)


A Square component.

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
- `fullscreenClassName` (String; optional): CSS class names to apply to the container.
- `fullscreen_style` (Dict; optional): Defines CSS styles for the container.
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `speedMultiplier` (Real; optional): The relative speed of the spinner
- `width` (Real; optional): The spinner width (in px)
"""
function dls_square(; kwargs...)
        available_props = Symbol[:children, :id, :color, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :show_initially, :speedMultiplier, :width]
        wild_props = Symbol[]
        return Component("dls_square", "Square", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_square(children::Any; kwargs...) = dls_square(;kwargs..., children = children)
dls_square(children_maker::Function; kwargs...) = dls_square(children_maker(); kwargs...)

