from flask import Flask
from getData import getWeatherInfo


weather_app = Flask(__name__)
@weather_app.route("/")
def weather():
    # get Location parameter From POST HTTP REQUEST
    # get Weather Data
    res = getWeatherInfo(1, 2)
    
    
    return res

if __name__ == "__main__":
    weather_app.run(debug=True)


