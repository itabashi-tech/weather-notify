import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def main():
    api_key = os.environ['WEATHER_API_KEY']
    line_notify_api = os.environ['WEATHER_NOTIFY_URL']
    params = {
        ## 緯度・軽度を指定する場合
        "lat": os.environ['LATITUDE'],
        "lon": os.environ['LONGITUDE'],
        ## 都市を指定する場合
        # "q": os.environ['LOCATION_OKINAWA'],
        "appid": api_key,
        "units": "metric",
        "lang": "ja",
    }
    try:        
        res = requests.get(line_notify_api, params=params)
        if res.status_code == 200:
            print("success get weather")
            data = json.loads(res.text)["main"]
            weather = json.loads(res.text)["weather"][0]
            return {
                "humidity": "湿度: " + str(data['humidity']) + "%",
                "temp": "気温: " + str(data['temp']) + "℃",
                "temp_max": "最高気温: " + str(data['temp_max']) + "℃",
                "temp_min": "最低気温: " + str(data['temp_min']) + "℃" ,
                "pressure": "気圧: " + str(data['pressure']) + "hPa",
                "weather": "天気: " + weather['main'] + "、" + weather['description'],
            }
    except Exception as e:
        print("get weather api exception")
        print(e)
        pass
