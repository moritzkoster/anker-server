import json

import requests
from bs4 import BeautifulSoup
from datetime import date

import python.util as util

@util.cache1d
def coop_info(name):
    with open("data/coop.json", "r") as file: #Get scraper data
        coop = json.load(file) #parse json

    url = coop[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs={coop[name]["attr_key"]: coop[name]["attr_value"]}) #find promotion field
    if promotion_field == None: #if Promotion
        return "kei Aktion"
    elif "53%" in promotion_field.get_text():
        return "Anker Halbe Priis"
    return "Anker aktion aber ned halbe priis."

@util.cache1d
def denner_info(name):
    return "this is the return value value of denner for: " + name #TODO