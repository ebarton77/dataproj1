#!/usr/bin/env python3
import uvicorn as uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import boto3
import requests

app = FastAPI()


# Model data you are expecting.
# Set defaults, data types, etc.
class Item(BaseModel):
    description: Optional[str] = None


@app.get("/")  # zone apex
def read_root():
    return {"Hello": "wonderful DS3002 professor and TA"}


@app.get("/disney")
def get_temp():
    LAT="28.5383"
    LON="-81.3792"
    KEY="6e3313543740951245a1a23b5a7d2491"
    units="Fahrenheit"
    url="https://api.openweathermap.org/data/2.5/weather?lat=" +LAT+"&lon=" + LON+"&appid=" + KEY
    response=requests.get(url)
    current=response.json()['main']['temp']
    current= round((int(current) *1.8 )- 459.67,2)
    feels = response.json()['main']['feels_like']
    feels=round((int(feels) *1.8 )- 459.67,2)
    description=response.json()['weather'][0]['description']
    return {"Current Disney Temp": current, "Feels Like": feels, "Units": units, "Description": description}

@app.get("/cville")
def get_temp():
    LAT="38.0293"
    LON="-78.4767"
    KEY="6e3313543740951245a1a23b5a7d2491"
    units="Fahrenheit"
    url="https://api.openweathermap.org/data/2.5/weather?lat=" +LAT+"&lon=" + LON+"&appid=" + KEY
    response=requests.get(url)
    current=response.json()['main']['temp']
    current= round((int(current) *1.8 )- 459.67,2)
    feels = response.json()['main']['feels_like']
    feels=round((int(feels) *1.8 )- 459.67,2)
    description=response.json()['weather'][0]['description']
    return {"Current C-ville Temp": current, "Feels Like": feels, "Units": units, "Description": description}

@app.get("/weather/{zip_code}")
def get_temp2(zip_code:int, country_code:str,units:str,lang:str, max_min_temp: bool):
    API_KEY="6e3313543740951245a1a23b5a7d2491"
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=" +str(units)+ "&lang=" +str(lang)
    response=requests.get(url)
    current=response.json()['main']['temp']
    feels = response.json()['main']['feels_like']
    description = response.json()['weather'][0]['description']
    max_temp=response.json()['main']['temp_max']
    min_temp=response.json()['main']['temp_min']
    if max_min_temp== True:
        return {"Current Temp in the " + str(zip_code) + " zip code": current, "Feels like": feels,
                "Description": description, "Maximum Temp":max_temp, "Minimum Temp":min_temp}
    return {"Current Temp in the "+str(zip_code) +" zip code": current, "Feels like": feels, "Description":description}
