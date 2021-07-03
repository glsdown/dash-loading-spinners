# Individual Component Page:
# - Example of the component
# - Example of source code for the component
# - Props for the component

from docs_app.app import app
from docs_app.component_parser import COMPONENT_NAMES, get_component_details

components = {
    name: get_component_details(app, name) for name in COMPONENT_NAMES
}
