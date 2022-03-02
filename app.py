from flask import Flask
from read_weather import parseJson
import json

ENV = "DEV"

my_app = Flask(__name__)

if ENV == "DEV":
    my_app.debug = True

@my_app.route("/api/v1/results")
def main():
    return json.loads(parseJson())

