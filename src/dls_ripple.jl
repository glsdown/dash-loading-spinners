# AUTO GENERATED FILE - DO NOT EDIT

export dls_ripple

"""
    dls_ripple(;kwargs...)
    dls_ripple(children::Any;kwargs...)
    dls_ripple(children_maker::Function;kwargs...)


A Ripple component.

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
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `thickness` (Real; optional): The line thickness of the circles
- `width` (Real; optional): The width of the spinner (in px).
"""
function dls_ripple(; kwargs...)
        available_props = Symbol[:children, :id, :color, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :show_initially, :thickness, :width]
        wild_props = Symbol[]
        return Component("dls_ripple", "Ripple", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_ripple(children::Any; kwargs...) = dls_ripple(;kwargs..., children = children)
dls_ripple(children_maker::Function; kwargs...) = dls_ripple(children_maker(); kwargs...)
