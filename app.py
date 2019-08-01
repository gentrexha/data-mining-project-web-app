# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Globals

# Load data
# TODO(Fix this import)
df = pd.read_csv("data/datarrethpartive.csv")

# html layout
# TODO(Find out what this is actually for)
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
)

# Create controls
# TODO()

# Create app Layout
app.layout = html.Div(
    children=[
        # Error Message
        html.Div(id="error-message"),
        # Top Banner
        html.Div(
            className="study-browser-banner row",
            children=[
                html.H2(className="h2-title", children="Data Mining Project"),
                html.Div(
                    className="div-logo",
                    children=html.Img(
                        className="logo", src=app.get_asset_url("images/logo_version_3.png")
                    ),
                ),
                html.H2(className="h2-title-mobile", children="Data Mining Project"),
            ],
        ),
        # Body of the App
        html.Div(className="row app-body", children=[]),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
