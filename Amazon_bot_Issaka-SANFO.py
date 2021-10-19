"""
Bot app
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


"""
=====================================================================
"""

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server
# ====================================================================


buttons = html.Div(
    [
        dbc.Button("Launch Bot", color="success", className="mr-1", id="submit"),
    ]
)

inputs = html.Div(
    children=[
        html.Label('Please enter product name like: drone,shoes,car,copy book...'),
        html.Br(),
        dcc.Input(placeholder="Type here...", id="input"),
    ])

messages = html.Div(id = "message")

controle = dbc.Card(
    [
        dbc.FormGroup([inputs]),
    ],
    className="m-4 px-2",
)

controls = dbc.Card(
    [
        html.Br(),
        dbc.FormGroup([buttons]),
    ],
    className="m-4 px-2",
)

control = dbc.Card(
    [
        html.Br(),
        dbc.FormGroup([messages]),
    ],
    className="m-4 px-2"
)



app.layout = dbc.Container(
    [
        html.Div(children=[
            html.H1("BestBot for Amazon Shopping", className="bg-primary text-white"),
            html.Hr(),
            html.Img(src='assets/img/bot.jpg', width="300",height="200"),
            controle,
            controls,
            html.Hr(),
            control
        ],
        className="form-group text-center")
    ],
    fluid=True,
)



@app.callback(
  Output("message","children"),
  Input("input","value"),
  Input("submit","n_clicks")
)



def send_to_cart(input,submit):
  changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
  if "submit" in changed_id:
    driver = webdriver.Chrome('./chromedriver')
    time.sleep(2)
    driver.get("https://www.amazon.com")
    search_bar = driver.find_element_by_name("field-keywords")
    time.sleep(2)
    for letter in input:
      time.sleep(0.3)
      search_bar.send_keys(letter)
    time.sleep(3)
    search_bar.send_keys(Keys.RETURN) # click enter
    result = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a')[0]
    result.click()
    driver.find_element_by_id("add-to-cart-button").click()
                            
    return "Look at the Browser, "+str(input)+" is added to cart successfully!"
        
    


if __name__ == "__main__":
    app.run_server(debug=True)

"""
By Issaka SANFO

"""