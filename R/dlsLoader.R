# AUTO GENERATED FILE - DO NOT EDIT

dlsLoader <- function(children=NULL, id=NULL, color=NULL, coverClassName=NULL, cover_style=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, height=NULL, margin=NULL, radius=NULL, show_initially=NULL, size=NULL, speedMultiplier=NULL, spinnerCSS=NULL, type=NULL, width=NULL) {
    
    props <- list(children=children, id=id, color=color, coverClassName=coverClassName, cover_style=cover_style, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, height=height, margin=margin, radius=radius, show_initially=show_initially, size=size, speedMultiplier=speedMultiplier, spinnerCSS=spinnerCSS, type=type, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Loader',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'coverClassName', 'cover_style', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'height', 'margin', 'radius', 'show_initially', 'size', 'speedMultiplier', 'spinnerCSS', 'type', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
