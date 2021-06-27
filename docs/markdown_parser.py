import re
from pathlib import Path

import dash_loading_spinners as dls
import dash_core_components as dcc
import dash_html_components as html

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


def create_adjustable_component(component, component_name, attributes):

    component_name = component_name.lower()
    # TODO: Consider how to allow the end user to adjust the attributes
    for attribute in attributes:
        pass
    return html.Div(component(id=f"example-{component_name}"), className="m-5")


def get_component_details(component_name):
    component = getattr(dls, component_name)
    component_doc = component.__doc__

    return_div = [
        dcc.Markdown("### Keyword arguments for {}".format(component_name))
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
    attributes = ["fullscreen", "debounce"]
    sorted_docs = {v.split("`**")[0]: "**`" + v for v in docs.split("**`")}
    for k in sorted(sorted_docs):
        if len(k.strip()) == 0:
            continue
        if k in COMMON_PROPS:
            core_components.append(sorted_docs[k])
        else:
            specialised_components.append(sorted_docs[k])
            attributes.append(k)

    # create an example of the component
    return_div.append(
        create_adjustable_component(component, component_name, attributes)
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
