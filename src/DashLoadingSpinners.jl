
module DashLoadingSpinners
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("dls_rsbeat.jl")
include("dls_rsbounce.jl")
include("dls_rscircle.jl")
include("dls_rsclimbingbox.jl")
include("dls_rsclip.jl")
include("dls_rsclock.jl")
include("dls_rsdot.jl")
include("dls_rsfade.jl")
include("dls_rsgrid.jl")
include("dls_rshash.jl")
include("dls_rsmoon.jl")
include("dls_rspacman.jl")
include("dls_rspropagate.jl")
include("dls_rspuff.jl")
include("dls_rspulse.jl")
include("dls_rsring.jl")
include("dls_rsrise.jl")
include("dls_rsrotate.jl")
include("dls_rsscale.jl")
include("dls_rssync.jl")

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
