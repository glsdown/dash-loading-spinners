# AUTO GENERATED FILE - DO NOT EDIT

dlsCustom <- function(children=NULL, id=NULL, debounce=NULL, fullscreen=NULL, fullscreenClassName=NULL, fullscreen_style=NULL, show_initially=NULL, svg=NULL, width=NULL) {
    
    props <- list(children=children, id=id, debounce=debounce, fullscreen=fullscreen, fullscreenClassName=fullscreenClassName, fullscreen_style=fullscreen_style, show_initially=show_initially, svg=svg, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Custom',
        namespace = 'dash_loading_spinners',
        propNames = c('children', 'id', 'debounce', 'fullscreen', 'fullscreenClassName', 'fullscreen_style', 'show_initially', 'svg', 'width'),
        package = 'dashLoadingSpinners'
        )

    structure(component, class = c('dash_component', 'list'))
}
