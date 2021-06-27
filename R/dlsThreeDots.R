# AUTO GENERATED FILE - DO NOT EDIT

dlsThreeDots <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, height=NULL, radius=NULL, secondaryColor=NULL, show_initially=NULL, speed_multiplier=NULL, tertiaryColor=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, height=height, radius=radius, secondaryColor=secondaryColor, show_initially=show_initially, speed_multiplier=speed_multiplier, tertiaryColor=tertiaryColor, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ThreeDots',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'radius', 'secondaryColor', 'show_initially', 'speed_multiplier', 'tertiaryColor', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
