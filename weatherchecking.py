import json

import requests

# Ask the user input from the useer
city=input('Enter a city name:')

#Api details
base_url="http://api.openweathermap.org/data/2.5/weather"
api_key="a8eb4946b9809b542026f85789cee83d"

#parameters are  inputs for the api
A={
    "q":city,
    "appid":api_key,
    "units":"metric"
}

#how do i finally make a api call or requests
response=requests.get(base_url,A)
data=response.json()
print(json.dumps(data,indent=3))
D=data["weather"][0]["description"]
T=data["main"]["temp"]
print(f"The current temperature of the {city} is {T} and its {D}")