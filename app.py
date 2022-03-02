from flask import Flask
from read_weather import parseJson
import json

ENV = "PROD"

my_app = Flask(__name__) # main flask object

# environment check
if ENV == "DEV":
    my_app.debug = True

# home route
@my_app.route("/")
def root():
    return "Please go to /api/v1/results to find the results you are looking for"

# main results route
@my_app.route("/api/v1/results")
def result():
    return json.loads(parseJson())

