# DS3002 Data Project 1: API Chatbot

## Summary of Functions
### My API has 3 endpoints, two of which require no parameters and retreive the current temperature and other information about my two favorite places: Disney World and Charlottesville. The last endpoint requires 5 user-inputted parameters that retreive weather information from ANY zip code!

## Endpoint #1:
### /disney
### This provides the current temperature in Orlando as well as what the temperature feels like, a description of the weather, and the units of measurement for the weather

## Endpoint #2:
### /cville
### This provides the current temperature in Charlottesville as well as what the temperature feels like, a description of the weather, and the units of measurement for the weather

## Endpoint #3
### /weather/{zip_code},{country_code}
### There are 5 parameters for this endpoint:
#### 1. zip_code: must be a valid zip code of type integer
#### 2. country_code: must be a valid two-letter country code (all valid country codes can be found in the country_codes.txt file)
#### 3. units: this represents the units of measurement the weather will be in. Valid units of measurement are: "standard", "imperial", or "metric". 
#### 4. lang: this represents the language you will receive your information in. Must be a valid language code (all valid language codes can be found in the language_codes.txt file)
#### 5. max_min_temp: must input a valid boolean. If you input True, the maximum and minimum temperature information will also be provides. If you input False, this additional information will not be provided

## Steps to run the container: 
### 1. git clone  https://github.com/ebarton77/dataproj1.git 
### 2. cd dataproj1 locally
### 3. docker run -it -v ${pwd}:/root/dataproj1 ebarton77/fastapi:latest 
### It will automatically startup the fastapi and you can copy the link into your browser
### Make sure to pull the lastest version first: docker pull ebarton77/fastapi:latest


## If you have any further issues, check /docs for more information or any error message that might have popped up

# Enjoy!

