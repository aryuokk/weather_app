# Importing important libaries required

import requests
import json
from config import weatherAPI

# Mandatory variable API

API = weatherAPI # Get it from weatherapi.com

# Arguments to exit
q_li = ['q', 'Q', 'Quit', 'QUIT', 'quit', 'e', 'E', 'Exit', 'EXIT', 'exit']

# Loop to call the function repeatedly 
APP = True

while APP:
    print("\n# Enter location name to gets its weather information. #")
    print("To quit the app simply press q or Q")
    city_name = input(":- ")

    if city_name in q_li:
        print("Exiting APP...")
        APP = False

    else:
        try:
            url = f"https://api.weatherapi.com/v1/current.json?key={API}&q={city_name}" # API call

            result = requests.get(url) # Will call the website and fetch information

            wdic = json.loads(result.text) # Makes the result more readable with json module

            # Every possible information will be fetched from here
            
            # Location vars
            name = wdic["location"]["name"]
            region = wdic["location"]["region"]
            country = wdic["location"]["country"]
            tz_id = wdic["location"]["tz_id"]
            localtime = wdic["location"]["localtime"]

            # Current vars
            temp_c = wdic["current"]["temp_c"]
            wind_kph = wdic["current"]["wind_kph"]
            wind_degree = wdic["current"]["wind_degree"]
            wind_dir = wdic["current"]["wind_dir"]
            precip_mm = wdic["current"]["precip_mm"]
            humidity = wdic["current"]["humidity"]
            cloud = wdic["current"]["cloud"]
            uv = wdic["current"]["uv"]
            gust_kph = wdic["current"]["gust_kph"]
            
            # Result formating
            msg = f'''\n---> LOCATION DETAILS <---
Location entered : {city_name}
Name : {name}
Region : {region}
Country : {country}
Timezone : {tz_id}
Local Date Time : {localtime}

---> WEATHER DETAILS <---
Temperature in C : {temp_c}
Humidity : {humidity}
Cloud : {cloud}
UV rays : {uv}
Wind k/h : {wind_kph}
Wind direction : {wind_dir}
Wind degree : {wind_degree}
Precipitaion in mm : {precip_mm}
Gust k/h : {gust_kph}
'''

            # Result printing
            print(msg)

        
        # To escape error
        except Exception as e:
            print(e)
            # print(f"\nName : {city_name}\nInavild City name or City data not present in database\n")