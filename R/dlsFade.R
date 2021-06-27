# AUTO GENERATED FILE - DO NOT EDIT

dlsFade <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, show_initially=NULL, speed_multiplier=NULL, thickness=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, show_initially=show_initially, speed_multiplier=speed_multiplier, thickness=thickness, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Fade',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'speed_multiplier', 'thickness', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
