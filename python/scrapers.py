import json

import requests
from bs4 import BeautifulSoup
from datetime import date

import python.util as util
# coop = {"anker": {"url": 'https://www.coop.ch/de/lebensmittel/getraenke/bier/multipacks-ab-12x50cl/anker-lager-bier-24x50cl/p/3458809', "attr_key": "data-testauto", "attr_value": "productlistpromotion3458809"},
        # "soja_sauce": {"url": ""}}

@util.cache1d
def coop_info(name):
    with open("data/coop.json", "r") as file:
        coop = json.load(file)
    url = coop[name]["url"]
    print(url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs={coop[name]["attr_key"]: coop[name]["attr_value"]})
    if promotion_field == None:
        return "kei Aktion"
    elif "53%" in promotion_field.get_text():
        return "Anker Halbe Priis"
    return "Anker aktion aber ned halbe priis."

@util.cache1d
def testfunction(name):
    return "this is the thest value"
