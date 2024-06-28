import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

from data_prep import df, countries, years
ui.h1("Electricity Generation Emissions Dashboard")

with ui.sidebar():
    ui.input_select('country', 'Select Country', countries)
    ui.input_slider('year', 'Select Year', years[0], years[-1],2022)


@render_plotly
def plot1():
    return px.bar(df[df.country == input.country()], x="year", y="emissions_quantity")
