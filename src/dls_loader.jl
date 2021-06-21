# AUTO GENERATED FILE - DO NOT EDIT

export dls_loader

"""
    dls_loader(;kwargs...)
    dls_loader(children::Any;kwargs...)
    dls_loader(children_maker::Function;kwargs...)


A Loader component.

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
- `fullscreenClassName` (String; optional): Often used with CSS to style elements with common properties.
- `fullscreen_style` (Dict; optional): Defines CSS styles for the container when fullscreen=True.
- `height` (Real; optional): The spinner height (in px) - only applicable for loaders of type:
- bar
- fade
- scale
- `margin` (Real; optional): The spinner margin (in px) - only applicable for loaders of type:
- beat
- dot
- fade
- hash
- moon
- pacman
- pulse
- ring
- rise
- rotate
- scale
- sync
- `radius` (Real; optional): The spinner radius (in px) - only applicable for loaders of type:
- fade
- scale
- `show_initially` (Bool; optional): Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.
- `size` (Real; optional): The spinner size (in px) - not applicable for loaders of type:
- bar
- fade
- scale
- `speedMultiplier` (Real; optional): The relative speed of the spinner
- `spinnerCSS` (Dict; optional): Defines additional CSS styles for the spinner itself. It's based on the
emotion css styles here: https://emotion.sh/docs/introduction
- `spinnerClassName` (String; optional): CSS class names to apply to the container when fullscreen=False.
- `spinner_style` (Dict; optional): Defines CSS styles for the container when fullscreen=False.
- `type` (String; optional): The type of spinner. Options are:
- bar
- beat
- bounce
- circle
- climbingBox
- clip
- clock
- dot
- fade
- grid
- hash
- moon
- pacman
- propagate
- puff
- pulse
- ring
- rise
- rotate
- scale
- sync
- `width` (Real; optional): The spinner width (in px) - only applicable for loaders of type:
- bar
- fade
- scale
"""
function dls_loader(; kwargs...)
        available_props = Symbol[:children, :id, :color, :debounce, :fullscreen, :fullscreenClassName, :fullscreen_style, :height, :margin, :radius, :show_initially, :size, :speedMultiplier, :spinnerCSS, :spinnerClassName, :spinner_style, :type, :width]
        wild_props = Symbol[]
        return Component("dls_loader", "Loader", "dash_loading_spinners", available_props, wild_props; kwargs...)
end

dls_loader(children::Any; kwargs...) = dls_loader(;kwargs..., children = children)
dls_loader(children_maker::Function; kwargs...) = dls_loader(children_maker(); kwargs...)

