# AUTO GENERATED FILE - DO NOT EDIT

export dls_custom

"""
    dls_custom(;kwargs...)
    dls_custom(children::Any;kwargs...)
    dls_custom(children_maker::Function;kwargs...)


A Custom component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component.
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `debounce` (Real; optional): When using the spinner as a loading spinner, add a time delay (in ms) to
the spinner being removed to prevent flickering.
- `fullscreen` (Bool; optional): Boolean that determines if the loading spinner will be displayed
full-screen or not.
- `fullscreenClassName` (String; optional): CSS class names to apply to the container when in fullscreen.
- `fullscreen_style` (Dict; optional): Defines CSS styles for the container when in fullscreen.
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `svg` (String; optional): The SVG code to include as the spinner, including required animations.
- `width` (Real; optional): The width of the resultant SVG (in px)

This helps to identify how big the covering div should be.
"""
function dls_custom(; kwargs...)
        available_props = Symbol[:children, :id, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :show_initially, :svg, :width]
        wild_props = Symbol[]
        return Component("dls_custom", "Custom", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_custom(children::Any; kwargs...) = dls_custom(;kwargs..., children = children)
dls_custom(children_maker::Function; kwargs...) = dls_custom(children_maker(); kwargs...)

