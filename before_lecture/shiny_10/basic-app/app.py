from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    #ui.input_slider("n2", "N", 50, 500, 100),
    ui.output_text_verbatim("txt"),
)

# - `"n"`: value from user input
# - `"N"`: label 
# - `0`: minimum of slider
# - `100`: maximum of slider
# - `20`: default value of slider 
# - H[Link to sliderInput documentation](https://shiny.posit.co/r/reference/shiny/0.14/sliderinput)



def server(input, output, session): #`shinywidgets` has its own UI output element: `output_widget()`
    @render.text # - *Syntax for rendering output*: render decorators like `@render.plot`,  `@render.table`, '@render.altair'
    def txt(): # - *Syntax for defining output*: `def value():` on server side becomes `"value"` on UI side
        return f"n*2 is {input.n() * 2}" # - *Syntax for defining input*: `"x"` on UI side becomes `input.x()` on server side

        #+ "& n2 is {input.n2()}"


# -  Shiny's syntax: `"txt"` on UI side corresponds to `txt()` on the server side
# \vspace{-1ex}
# - Additional syntax: `@render.text` indicates that `txt()` should be rendered as text

app = App(app_ui, server)

# - UI: ask user for `ui.input_slider("n")` 
# - Server: receive input as as `input.n()`
# - Server: compute `input.n() * 2`
# - Server: get output from server as `def txt():`
#     - We have to declare what this output will be eventually rendered as using a decorator (`@render.text`) 
# - UI: display output as `ui.output_text_verbatim("txt")`
