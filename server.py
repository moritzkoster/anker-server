from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS

import python.scrapers as scp

app = app = Flask(__name__, static_url_path="")

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

@app.route('/static/<path:path>')
def file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
