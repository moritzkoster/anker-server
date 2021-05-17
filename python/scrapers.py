import json

import requests
from bs4 import BeautifulSoup
from datetime import date

import python.util as util

@util.cache1d("coop")
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

@util.cache1d("denner")
def denner_info(name):
    with open("data/denner.json", "r") as file: #Get scraper data
        denner = json.load(file) #parse json

    url = denner[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs={denner[name]["attr_key"]: denner[name]["attr_value"]})
    if not promotion_field: #if Promotion
        return "kei Aktion"
    elif "42%" in promotion_field.get_text():
        return "Anker isch 42%, los chauf!!!"
    return "Anker aktion aber ned halbe priis."
