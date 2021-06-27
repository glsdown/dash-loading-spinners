# Individual Component Page:
# - Example of the component
# - Example of source code for the component
# - Props for the component

import dash_loading_spinners as dls

from component_parser import get_component_details, COMPONENT_NAMES


components = {name: get_component_details(name) for name in COMPONENT_NAMES}
