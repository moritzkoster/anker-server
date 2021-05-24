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

    promotion_field= soup.find(attrs=coop[name]["attrs"]) #find promotion field
    if promotion_field == None: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Coop")

@util.cache1d("denner")
def denner_info(name):
    with open("data/denner.json", "r") as file: #Get scraper data
        denner = json.load(file) #parse json

    url = denner[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=denner[name]["attrs"])
    if not promotion_field: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Denner")

@util.cache1d("spar")
def spar_info(name):
    with open("data/spar.json", "r") as file: #Get scraper data
        spar = json.load(file) #parse json

    url = spar[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=spar[name]["attrs"])
    if not promotion_field: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Spar")

def answer(name, prom, store):
    with open("data/" + name + ".json", "r") as file:
        aktion50 = json.load(file)
    text = random.choice(aktion50)
    return text.format(DISC=prom, STORE=store)
