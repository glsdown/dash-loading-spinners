import dash_bootstrap_components as dbc
from dash import html

layout = html.Div(
    dbc.Container(
        html.H1("404 - Not Found", className="text-danger"),
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)
