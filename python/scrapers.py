import json
import random
import requests
from bs4 import BeautifulSoup
from datetime import date

import python.util as util

@util.cache1d("coop")
def coop_info(name):
    coop = get_json("data/coop.json")

    url = coop[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=coop[name]["attrs"]) #find promotion field
    if promotion_field == None: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Coop")

@util.cache1d("denner")
def denner_info(name):
    denner = get_json("data/denner.json")

    url = denner[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=denner[name]["attrs"])
    if not promotion_field: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Denner")

@util.cache1d("spar")
def spar_info(name):
    spar = get_json("data/spar.json")

    url = spar[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=spar[name]["attrs"])
    if not promotion_field: #if Promotion
        return "NOPROM"
    return answer(name, promotion_field.get_text(), "Spar")

@util.cache1d("migros")
def migros_info(name):
    migros = get_json("data/migros.json")

    url = migros[name]["url"]
    html_text = requests.get(url).text #get html page
    soup = BeautifulSoup(html_text, 'html.parser')

    promotion_field= soup.find(attrs=migros[name]["attrsP"])
    if not promotion_field: #if Promotion
        return "NOPROM"
    usual_field= soup.find(attrs=migros[name]["attrsU"])
    try:
        current = float(promotion_field.get_text())
        usual = float(usual_field.get_text()[23:])
        return answer(name, f'{(1 -current/usual) *100 :.2f}%', "Migros")
    except:
        return "PROM but cold not calculate it"

def answer(name, prom, store):
    # with open("data/" + name + ".json", "r") as file:
    #     aktion50 = json.load(file)
    # text = random.choice(aktion50)
    #return text.format(DISC=prom, STORE=store)
    return prom

def get_json(path): # I know this is shit but dont know how to change it.
    try:
        with open(path, "r") as file: #try if its in working directory
            return json.load(file)
    except:
        with open(f"/var/www/anker-server/{path}", "r") as file: # else use static path.
            return json.load(file)
