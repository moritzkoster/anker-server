import json
import random
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
        return "NOPROM"
    return prom_answer(promotion_field.get_text(), "Coop")

@util.cache1d("denner")
def denner_info(name):
    with open("data/denner.json", "r") as file: #Get scraper data
        denner = json.load(file) #parse json

    url = denner[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs={denner[name]["attr_key"]: denner[name]["attr_value"]})
    if not promotion_field: #if Promotion
        return "NOPROM"
    return prom_answer(promotion_field.get_text(), "Denner")

def prom_answer(prom, store):
    with open("data/textsDE.json", "r") as file:
        aktion50 = json.load(file)
    text = random.choice(aktion50)
    return text.format(DISC=prom, STORE=store)
