import argparse
import requests
import pyfiglet

#API Key for openWeatherMap
API_KEY = '4dc1a401f34927bac2dbf2cba6dd59a9'
#Base URL for openWeatherMap API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#Mapping of weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

parser = argparse.ArgumentParser(description="Check the weather for a certain country/city.")
parser.add_argument("country", help="the country/city to check the weather for")
args = parser.parse_args()

# Construct API URL with query parameters
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print("Error: Unable to retrieve weather information.")
    exit()
data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct output with weather icon
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print output
print(output)