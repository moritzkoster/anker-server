from flask import Flask, request, render_template, send_from_directory
import json
import os
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from datetime import date

import python.util as util

app = app = Flask(__name__)

coop = {"anker": {"url": 'https://www.coop.ch/de/lebensmittel/getraenke/bier/multipacks-ab-12x50cl/anker-lager-bier-24x50cl/p/3458809', "attr_key": "data-testauto", "attr_value": "productlistpromotion3458809"}}

@app.route("/anker")
def anker():
    return coop_info("anker")

@util.cache1d
def coop_info(name):
    vgm_url = coop[name]["url"]
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs={coop[name]["attr_key"]: coop[name]["attr_value"]})
    if promotion_field == None:
        return "kei Aktion"
    elif "53%" in promotion_field.get_text():
        return "Anker Halbe Priis"
    return "Anker aktion aber ned halbe priis."

if __name__ == "__main__":
    app.run()
