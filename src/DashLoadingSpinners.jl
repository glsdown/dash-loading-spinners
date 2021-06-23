
module DashLoadingSpinners
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("dls_beat.jl")
include("dls_bounce.jl")
include("dls_circle.jl")
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
include("dls_sync.jl")

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
