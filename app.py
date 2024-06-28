import plotly.express as px
from shiny.express import input, ui
from shiny import reactive
from shinywidgets import render_plotly

from data_prep import df, countries, years, gases
ui.h1("Transportation Emissions Dashboard")
ui.p("Transportation Emissions Data by Country from climatetrace.org")

with ui.sidebar():
    ui.input_selectize('country', 'Select Country', countries, multiple=True)
    #ui.input_slider('year', 'Select Year', years[0], years[-1],2022)
    ui.input_select('gas', 'Select Gas', gases)

@reactive.calc
def filter_data():
    mask = (df.country.isin(input.country())) & (df.gas == input.gas())
    return df[mask]

@render_plotly
def plot1():
    return px.bar(filter_data(), 
                  x="year", 
                  y="emissions_quantity", 
                  color="country",
                barmode='group')
