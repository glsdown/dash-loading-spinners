% Auto-generated: do not edit by hand
\name{dlsRipple}

\alias{dlsRipple}

\title{Ripple component}

\description{

}

\usage{
dlsRipple(children=NULL, id=NULL, color=NULL, debounce=NULL,
fullscreen=NULL, fullscreenClassName=NULL,
fullscreen_style=NULL, show_initially=NULL, thickness=NULL,
width=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of this component.}

\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{color}{Character. Sets the color of the Spinner. You can also specify any valid CSS color
of your choice (e.g. a hex code, a decimal code or a CSS color name).

If not specified will default to black.}

\item{debounce}{Numeric. When using the spinner as a loading spinner, add a time delay (in ms) to
the spinner being removed to prevent flickering.}

\item{fullscreen}{Logical. Boolean that determines if the loading spinner will be displayed
full-screen or not.}

\item{fullscreenClassName}{Character. CSS class names to apply to the container when in fullscreen.}

\item{fullscreen_style}{Named list. Defines CSS styles for the container when in fullscreen.}

\item{show_initially}{Logical. Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.}

\item{thickness}{Numeric. The line thickness of the circles}

\item{width}{Numeric. The width of the spinner (in px).}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

