% Auto-generated: do not edit by hand
\name{dlsLoader}

\alias{dlsLoader}

\title{Loader component}

\description{

}

\usage{
dlsLoader(children=NULL, id=NULL, color=NULL, debounce=NULL,
fullscreen=NULL, fullscreenClassName=NULL,
fullscreen_style=NULL, height=NULL, margin=NULL,
radius=NULL, show_initially=NULL, size=NULL,
spinnerClassName=NULL, spinner_style=NULL, type=NULL,
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

\item{fullscreenClassName}{Character. Often used with CSS to style elements with common properties.}

\item{fullscreen_style}{Named list. Defines CSS styles for the container when fullscreen=True.}

\item{height}{Numeric. The spinner height (in px) - only applicable for loaders of type:
- bar
- fade
- scale}

\item{margin}{Numeric. The spinner margin (in px) - only applicable for loaders of type:
- beat
- dot
- fade
- hash
- moon
- pacman
- pulse
- ring
- rise
- rotate
- scale
- sync}

\item{radius}{Numeric. The spinner radius (in px) - only applicable for loaders of type:
- fade
- scale}

\item{show_initially}{Logical. Whether the Spinner should show on app start-up before the loading state
has been determined. Default True.}

\item{size}{Numeric. The spinner size (in px) - not applicable for loaders of type:
- bar
- fade
- scale}

\item{spinnerClassName}{Character. CSS class names to apply to the spinner.}

\item{spinner_style}{Named list. Inline CSS styles to apply to the spinner.}

\item{type}{Character. The type of spinner. Options are:
- bar
- beat
- bounce
- circle
- climbingBox
- clip
- clock
- dot
- fade
- grid
- hash
- moon
- pacman
- propagate
- puff
- pulse
- ring
- rise
- rotate
- scale
- sync}

\item{width}{Numeric. The spinner width (in px) - only applicable for loaders of type:
- bar
- fade
- scale}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

