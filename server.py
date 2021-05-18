from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS

# import json
# import os
#
# import requests
# from bs4 import BeautifulSoup
#
# from datetime import date
#
# import python.util as util
import python.scrapers as scp

app = app = Flask(__name__)

@app.route("/coop/<name>")
def coop(name):
    return scp.coop_info(name)


@app.route("/denner/<name>")
def denner(name):
    return scp.denner_info(name)


@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
