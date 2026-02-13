# Get Data From API
'''
    🌡️ temperature (now, hourly, daily)
    💧 humidity
    🌧️ rain / snow
    ☁️ clouds
    🌅 sunrise & sunset
    🌤️ weather condition (via code)
    📅 forecast for 10 days
'''
lan = 10
lon = 10

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

res = getWeather(1, 2)
print(res)
