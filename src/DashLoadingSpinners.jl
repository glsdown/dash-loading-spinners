
module DashLoadingSpinners
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("dls_custom.jl")
include("dls_dualring.jl")
include("dls_ellipsis.jl")
include("dls_hourglass.jl")
include("dls_ringchase.jl")
include("dls_ripple.jl")
include("dls_roller.jl")
include("dls_spinningdisc.jl")
include("dls_wave.jl")
include("dls_audio.jl")
include("dls_balltriangle.jl")
include("dls_bars.jl")
include("dls_circles.jl")
include("dls_gridfade.jl")
include("dls_hearts.jl")
include("dls_mutatingdots.jl")
include("dls_oval.jl")
include("dls_revolvingdot.jl")
include("dls_rings.jl")
include("dls_tailspin.jl")
include("dls_target.jl")
include("dls_threedots.jl")
include("dls_triangle.jl")
include("dls_beat.jl")
include("dls_bounce.jl")
include("dls_climbingbox.jl")
include("dls_clip.jl")
include("dls_clock.jl")
include("dls_dot.jl")
include("dls_fade.jl")
include("dls_grid.jl")
include("dls_hash.jl")
include("dls_moon.jl")
include("dls_pacman.jl")
include("dls_propagate.jl")
include("dls_puff.jl")
include("dls_pulse.jl")
include("dls_ring.jl")
include("dls_rise.jl")
include("dls_rotate.jl")
include("dls_scale.jl")
include("dls_skew.jl")
include("dls_square.jl")
include("dls_sync.jl")
include("dls_tunnel.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_loading_spinners",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_loading_spinners.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_loading_spinners.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
