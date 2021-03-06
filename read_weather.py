import json
from datetime import datetime


def parseJson():

    jsonFile = open("./weather.json") # getting the data from json file
    jsonData = json.load(jsonFile) # converting to json

    date = jsonData['current']['dt']
    sunrise = jsonData['current']['sunrise']
    sunset = jsonData['current']['sunset']

    dt = datetime.fromtimestamp(date).date()
    snrise = datetime.fromtimestamp(sunrise).time()
    snset = datetime.fromtimestamp(sunset).time()

    #  main json object we will return
    returnObject = {
        "status":"success",
        "Data":{
            "Dt": str(dt),
            "Sunrise_time": str(snrise),
            "Sunset_time": str(snset),
        }
    }

    # print(datetime.fromtimestamp(date).date())
    # print(datetime.fromtimestamp(sunrise).time())
    # print(datetime.fromtimestamp(sunset).time())

    return json.dumps(returnObject)