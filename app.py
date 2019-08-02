# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Globals

# Load data
df = pd.read_csv("data/datarrethkryetarevekomunave.csv")
df["Data"] = pd.to_datetime(df["Data"])

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
                        className="logo",
                        src=app.get_asset_url("images/logo_version_4.png"),
                    ),
                ),
                html.H2(className="h2-title-mobile", children="Data Mining Project"),
            ],
        ),
        # Body of the App
        html.Div(
            className="row app-body",
            children=[
                # User Controls
                html.Div(
                    className="four columns card",
                    children=[
                        html.Div(
                            className="bg-white user-control",
                            children=[
                                html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Municipality"),
                                        dcc.Dropdown(
                                            id="study-dropdown",
                                            options=[
                                                {
                                                    "label": "Prishtina",
                                                    "value": "Prishtina",
                                                },
                                                {
                                                    "label": "Gjakova",
                                                    "value": "Gjakova",
                                                },
                                            ],
                                            value="Prishtina",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Choose the type of comparison"),
                                        dcc.RadioItems(
                                            id="chart-type",
                                            options=[
                                                {"label": "Likes", "value": "NrLike"},
                                                {
                                                    "label": "Reactions",
                                                    "value": "NrReaction",
                                                },
                                                {
                                                    "label": "Comments",
                                                    "value": "NrKomenteve",
                                                },
                                                {"label": "Shares", "value": "NrShare"},
                                                {
                                                    "label": "Posts",
                                                    "value": "nrPosteve",
                                                },
                                            ],
                                            value="NrLike",
                                            labelStyle={
                                                "display": "inline-block",
                                                "padding": "12px 12px 0px 0px",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                # Graph
                html.Div(
                    className="eight columns card-left",
                    children=[
                        html.Div(
                            className="bg-white",
                            children=[
                                html.H5("Facebook Activity Graph"),
                                dcc.Graph(id="plot"),
                            ],
                        )
                    ],
                ),
                dcc.Store(id="error", storage_type="memory"),
            ],
        ),
    ]
)


# Callbacks
# Callback to generate activity data
@app.callback(
    Output("plot", "figure"),
    [Input("chart-type", "value"), Input("study-dropdown", "value")],
)
def update_output(chart_type, municipality):
    dff = df[df["Komuna"] == municipality]

    trace = []
    for candidate in dff["EmriKandidatit"].unique():
        trace.append(
            go.Scatter(
                x=dff["Data"],
                y=dff[chart_type].loc[df["EmriKandidatit"] == candidate],
                name=candidate,
                mode="lines",
                line_shape='linear',
                marker={"size": 8, "opacity": 0.6, "line": {"width": 0.5}},
            )
        )

    return {
        "data": trace,
        "layout": go.Layout(
            title="Amount of {} over time".format(chart_type),
            colorway=["#fdae61", "#abd9e9", "#2c7bb6"],
            yaxis={"title": "Amount of {}".format(chart_type)},
            xaxis={"title": "Date"},
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=True)
