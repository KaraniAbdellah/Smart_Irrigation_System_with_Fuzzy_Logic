from flask import Flask

weather_app = Flask(__name__)
@weather_app.route("/")
def getWeatherInfo():
    return "Weather Information ddd"


if __name__ == "__main__":
    weather_app.run(debug=True)


