import re

import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
from dash import Input, Output, dcc, html

__all__ = ["get_component_details"]

HEADER_PATTERN = re.compile(r"---.*---", flags=re.DOTALL)
SPLIT_PATTERN = re.compile(r"{{.*}}")
EXAMPLE_DOC_PATTERN = re.compile(r"{{(.*)}}")

# To format the docstrings
VERBATIM_PATTERN = re.compile(r"`((\\\[)((.|\n)*?)(\\]))`")
LINK_PATTERN = re.compile(r"\\\[([\w\.\-:\/]+)\\\]\(([\w\.\-:#\/]+)\)")
PROP_OPTIONAL_DEFAULT_PATTERN = re.compile(r"""default (.*)\)""")
PROP_TYPE_PATTERN = re.compile(r"""(\s*- \w+?\s*\()([^;]*);""")
PROP_NAME_PATTERN = re.compile(r"""(\n- )(\w+?) \(""")
NESTED_PROP_NAME_PATTERN = re.compile(r"""(\n\s+- )(\w+?) \(""")

COMPONENT_NAMES = [
    "Sync",
    "Pulse",
    "Pacman",
    "Grid",
    "Oval",
    "Moon",
    # "Custom",
    "Skew",
    "Wave",
    "Circles",
    "GridFade",
    "ClimbingBox",
    "MutatingDots",
    "Clock",
    "Tunnel",
    "Ellipsis",
    "Hash",
    "Bounce",
    "Triangle",
    "Puff",
    "RingChase",
    "Target",
    "BallTriangle",
    "Bars",
    "Audio",
    "TailSpin",
    "SpinningDisc",
    "Rings",
    "Dot",
    "ThreeDots",
    "Ripple",
    "Square",
    "Fade",
    "Clip",
    "Hearts",
    "Rotate",
    "Hourglass",
    "DualRing",
    "RevolvingDot",
    "Propagate",
    "Rise",
    "Ring",
    "Scale",
    "Beat",
    "Roller",
]


COMMON_PROPS = set(
    [
        "id",
        "debounce",
        "fullscreen",
        "children",
        "fullscreenClassName",
        "fullscreen_style",
        "show_initially",
    ]
)

PROP_ORDER = [
    "color",
    "secondaryColor",
    "tertiaryColor",
    "size",
    "width",
    "height",
    "radius",
    "thickness",
    "margin",
    "speed_multiplier",
    "svg",
]


def color_changer(app, component_name, attribute_name, default="#000000"):
    @app.callback(
        Output(f"example-{component_name}", attribute_name),
        [Input(f"colorpicker-{component_name}-{attribute_name}", "value")],
    )
    def temp(color):
        if not color:
            color = "#000000"
        return color.strip("'")

    return html.Div(
        [
            dbc.Label(
                [
                    html.Code(f"{attribute_name}"),
                ]
            ),
            dbc.Input(
                type="color",
                id=f"colorpicker-{component_name}-{attribute_name}",
                value=default,
                style={"width": 75, "height": 25},
                className="p-0 ml-3",
            ),
        ]
    )


def number_slider(app, component_name, attribute_name, default=0):

    app.clientside_callback(
        """
    function(value) {
        return value
    }
    """,
        Output(f"example-{component_name}", attribute_name),
        Input(f"slider-{component_name}-{attribute_name}", "value"),
    )

    if attribute_name in ["width", "size"]:
        maximum_value = 250
        step = 10
    elif attribute_name in ["height"]:
        maximum_value = 100
        step = 10
    elif attribute_name in ["speed_multiplier"]:
        maximum_value = 5
        step = 0.1
    elif attribute_name in ["radius"]:
        maximum_value = 16
        step = 2
    elif attribute_name in ["thickness"]:
        maximum_value = 20
        step = 1
    else:
        maximum_value = 10
        step = 1

    return html.Div(
        [
            dbc.Label([html.Code(f"{attribute_name}")]),
            dcc.Slider(
                id=f"slider-{component_name}-{attribute_name}",
                value=default,
                min=0,
                max=maximum_value,
                step=step,
                marks={
                    0: "0",
                    maximum_value / 2: str(maximum_value / 2),
                    maximum_value: str(maximum_value),
                },
                tooltip={"always_visible": True, "placement": "bottom"},
            ),
        ]
    )


def create_adjustable_component(app, component, component_name, attributes):

    component_name = component_name.lower()
    main_components = []

    for attribute, value in dict(
        sorted(attributes.items(), key=lambda k: PROP_ORDER.index(k[0]))
    ).items():
        if re.search("[cC]olor", attribute):
            main_components.append(
                color_changer(app, component_name, attribute, value)
            )
        elif attribute in [
            "width",
            "height",
            "size",
            "thickness",
            "margin",
            "radius",
            "speed_multiplier",
        ]:
            try:
                value = float(value)
            except TypeError:
                value = 0
            main_components.append(
                number_slider(app, component_name, attribute, value)
            )
        else:
            main_components.append(
                html.Div(f"attribute {attribute} with default {value}")
            )
    return dbc.Container(
        [
            dcc.Markdown("#### View custom properties"),
            dbc.Row(
                [
                    dbc.Col(component(id=f"example-{component_name}"), md=4),
                    dbc.Col(main_components, md=8),
                ]
            ),
        ],
        className="my-3 p-3 border rounded",
    )


def get_component_details(app, component_name):
    component = getattr(dls, component_name)
    component_doc = component.__doc__

    return_div = [
        dcc.Markdown("### Keyword arguments for {}".format(component_name)),
    ]

    docs = component_doc.split("Keyword arguments:")[-1]

    docs = re.sub(VERBATIM_PATTERN, r"`[\3]`", docs)

    # format links
    docs = re.sub(LINK_PATTERN, r"[\1](\2)", docs)

    # formats the prop defaults
    docs = re.sub(PROP_OPTIONAL_DEFAULT_PATTERN, r"default `\1`)", docs)

    # formats the prop type
    docs = re.sub(PROP_TYPE_PATTERN, r"\1*\2*;", docs)

    # formats the prop name on first level only
    docs = re.sub(PROP_NAME_PATTERN, r"\1**`\2`** (", docs)

    # formats keys of nested dicts
    docs = re.sub(NESTED_PROP_NAME_PATTERN, r"\1**`\2`** (", docs)

    # removes a level of nesting
    docs = docs.replace("\n-", "\n")

    # identify the different 'types' of attributes to be able to understand
    # them more easily
    core_components = []
    specialised_components = []
    attributes = {}
    split_docs = {v.split("`**")[0]: "**`" + v for v in docs.split("**`")}
    for k in split_docs:
        if len(k.strip()) == 0:
            continue
        if k in COMMON_PROPS:
            core_components.append(split_docs[k])
        else:
            if default := re.search(
                r"default `([a-zA-Z0-9\-_#'\"]+)`\)", split_docs[k]
            ):
                attributes.update({k: default.groups(1)[0]})
            else:
                attributes.update({k: None})
            specialised_components.append(split_docs[k])

    # create an example of the component
    return_div.append(
        create_adjustable_component(app, component, component_name, attributes)
    )

    # display the component specific attributes e.g. size, color
    return_div.append(
        dcc.Markdown(
            """#### Component specific keyword arguments

These are arguments that vary between components."""
        ),
    )
    return_div.append(dcc.Markdown("\n".join(specialised_components)))

    # display the more generic attributes e.g. fullscreen
    return_div.append(
        dcc.Markdown(
            """#### Core keyword arguments

These are arguments that are consistent between components."""
        ),
    )
    return_div.append(dcc.Markdown("\n".join(core_components)))

    # Return the full page
    return html.Div(return_div, className="reference")
