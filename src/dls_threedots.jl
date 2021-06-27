# AUTO GENERATED FILE - DO NOT EDIT

export dls_threedots

"""
    dls_threedots(;kwargs...)
    dls_threedots(children::Any;kwargs...)
    dls_threedots(children_maker::Function;kwargs...)


A ThreeDots component.
Three solid colour pulsing dots (optionally of different colours),
in a horizontal line.
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
- `height` (Real; optional): The spinner height (in px)
- `radius` (Real; optional): The radius of each dot (in px)
- `secondaryColor` (String; optional): Sets the color of the Spinner. You can also specify any valid CSS color
of your choice (e.g. a hex code, a decimal code or a CSS color name).

If not specified will default to blue.
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `speed_multiplier` (Real; optional): The relative speed of the spinner
- `tertiaryColor` (String; optional): Sets the color of the Spinner. You can also specify any valid CSS color
of your choice (e.g. a hex code, a decimal code or a CSS color name).

If not specified will default to green.
- `width` (Real; optional): The spinner width (in px)
"""
function dls_threedots(; kwargs...)
        available_props = Symbol[:children, :id, :color, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :height, :radius, :secondaryColor, :show_initially, :speed_multiplier, :tertiaryColor, :width]
        wild_props = Symbol[]
        return Component("dls_threedots", "ThreeDots", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_threedots(children::Any; kwargs...) = dls_threedots(;kwargs..., children = children)
dls_threedots(children_maker::Function; kwargs...) = dls_threedots(children_maker(); kwargs...)

