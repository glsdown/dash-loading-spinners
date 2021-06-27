# AUTO GENERATED FILE - DO NOT EDIT

dlsWave <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, show_initially=NULL, thickness=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, show_initially=show_initially, thickness=thickness, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Wave',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'thickness', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
