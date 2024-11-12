from shiny import App, render, ui

#import what is needed!!
from shinywidgets import render_altair, output_widget
import altair as alt
import numpy as np
import pandas as pd
import anywidget #sometimes may need

app_ui = ui.page_fluid(
    ui.panel_title("Histogram of 100 Draws from Normal with mean mu"), #add title
    ui.input_slider("mu", "N", 0, 100, 20), #add slider for input
    output_widget("my_hist") #display widget; defined below:
)

def server(input, output, session):
    # [other server-side code]
    @render_altair #render as an altair plot
    def my_hist(): #define altair plot
        sample = np.random.normal(input.mu(), 20, 100) #generate a sample
        df = pd.DataFrame({'sample': sample}) #put into df
        return(
            alt.Chart(df).mark_bar().encode( #return bar chart
                alt.X('sample:Q', bin=True), 
                alt.Y("count()")
            )
        )

app = App(app_ui, server)
