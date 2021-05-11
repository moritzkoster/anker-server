from flask import Flask, request, render_template, send_from_directory
import json
import os
from flask_cors import CORS
import python.util as util
from datetime import date

def cache1d(function):
    def wrapper(name):
        if last[name]["date"] == date.today():
            return last[name]["info"]
            print("already existed")
        else:
            info = function(name)
            last[name]["info"] = info
            last[name]["date"] = date.today()
            print("new request")
            return info
    return wrapper

@cache1d
def get_info(name):
    return "the holy Value"


last = {"anker": {"date": 0, "info": ""}}

print(get_info("anker"))
last["anker"]["info"] = "ha di verwütscht"
print(get_info("anker"))
