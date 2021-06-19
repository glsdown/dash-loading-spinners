# AUTO GENERATED FILE - DO NOT EDIT

dlsLoader <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, height=NULL, margin=NULL, radius=NULL, show_initially=NULL, size=NULL, spinnerClassName=NULL, spinner_style=NULL, type=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, height=height, margin=margin, radius=radius, show_initially=show_initially, size=size, spinnerClassName=spinnerClassName, spinner_style=spinner_style, type=type, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Loader',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'margin', 'radius', 'show_initially', 'size', 'spinnerClassName', 'spinner_style', 'type', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
