from flask import Flask
import requests


def getWeather(lan, log):
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": lan,
        "longitude": log,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    response = requests.get(url, params=params)
    return response.json()


app = Flask(__name__)
@app.router("/getData")
def getData(lan, log):
    getWeather(lan=lan, log=log)


