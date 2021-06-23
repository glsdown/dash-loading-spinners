# AUTO GENERATED FILE - DO NOT EDIT

dlsDot <- function(children=NULL, id=NULL, color=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, margin=NULL, show_initially=NULL, size=NULL, speedMultiplier=NULL, spinnerCSS=NULL) {
    
    props <- list(children=children, id=id, color=color, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, margin=margin, show_initially=show_initially, size=size, speedMultiplier=speedMultiplier, spinnerCSS=spinnerCSS)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Dot',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'color', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'margin', 'show_initially', 'size', 'speedMultiplier', 'spinnerCSS'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
