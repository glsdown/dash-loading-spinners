# Individual Component Page:
# - Example of the component
# - Example of source code for the component
# - Props for the component

import dash_core_components as dcc
import dash_loading_spinners as dls

from markdown_parser import get_component_details

from not_found import layout as not_found_layout


def layout(component_name):
    try:
        getattr(dls, component_name)
        return get_component_details(component_name)
    except:
        return not_found_layout
