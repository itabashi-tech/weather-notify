from api.getWeather import main as getWeather
from api.postLine import main as postLine
import json
import time

def main():
    try:
        print("start")
        newWeathers = getWeather()
        filePath = "./json/weather.json"
        try:
            with open(file=filePath, mode="r", encoding="utf-8_sig") as file:
                weathers = json.load(file)
                if weathers["weather"] == newWeathers["weather"] and weathers["humidity"] == newWeathers["humidity"] and weathers["temp"] == newWeathers["temp"] and weathers["pressure"] == newWeathers["pressure"] and weathers["temp_max"] == newWeathers["temp_max"] and weathers["temp_min"] == newWeathers["temp_min"]:
                    print("not update")
                else:
                    with open(file=filePath, mode="w", encoding="utf-8_sig") as file:
                        file.write(json.dumps(newWeathers))
                        postLine(newWeathers["weather"] + '\n' + '\n' + newWeathers["humidity"] + '\n' + newWeathers["temp"] + '\n' + newWeathers["pressure"] + '\n' + '\n' + newWeathers["temp_max"]+ '\n' + newWeathers["temp_min"])
        except Exception as e:
            print(e)
            print("file exception")
        
    except Exception as e:
        print(e)
        postLine("exception")

while True:
    main()
    time.sleep(3600)
