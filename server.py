from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS

import python.scrapers as scp

app = app = Flask(__name__)

@app.route("/coop/<name>")
def coop(name):
    return scp.coop_info(name)

@app.route("/denner/<name>")
def denner(name):
    return scp.denner_info(name)

@app.route("/spar/<name>")
def spar(name):
    return scp.spar_info(name)

@app.route("/")
def hello():
    return render_template("LmH_V1.html")

if __name__ == "__main__":
    app.run()
