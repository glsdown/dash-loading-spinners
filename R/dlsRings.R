# AUTO GENERATED FILE - DO NOT EDIT

dlsRings <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, height=NULL, radius=NULL, show_initially=NULL, speedMultiplier=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, height=height, radius=radius, show_initially=show_initially, speedMultiplier=speedMultiplier, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Rings',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'radius', 'show_initially', 'speedMultiplier', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
