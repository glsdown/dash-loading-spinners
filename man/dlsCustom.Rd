% Auto-generated: do not edit by hand
\name{dlsCustom}

\alias{dlsCustom}

\title{Custom component}

\description{
Create a custom spinner from an animated SVG
}

\usage{
dlsCustom(children=NULL, id=NULL, debounce=NULL, fullscreen=NULL,
fullscreenClassName=NULL, fullscreen_style=NULL,
show_initially=NULL, svg=NULL, width=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of this component.}

\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{debounce}{Numeric. When using the spinner as a loading spinner, add a time delay (in ms) to
the spinner being removed to prevent flickering.}

\item{fullscreen}{Logical. Boolean that determines if the loading spinner will be displayed
full-screen or not.}

\item{fullscreenClassName}{Character. CSS class names to apply to the container when in fullscreen.}

\item{fullscreen_style}{Named list. Defines CSS styles for the container when in fullscreen.}

\item{show_initially}{Logical. Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.}

\item{svg}{Character. The SVG code to include as the spinner, including required animations.}

\item{width}{Numeric. The width of the resultant SVG (in px)

This helps to identify how big the covering div should be.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

