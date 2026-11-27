import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
countries_api_key = os.getenv("RESTCOUNTRIES_API_KEY")

# If you want to save the weather data:

def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q"     : city,
        "appid" : api_key,
        "units" : "metric"
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None

def get_country_info(country_code):
    url = f"https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}"
    headers = {"Authorization": f"Bearer {countries_api_key}"}
    params = {"response_fields": "names.common,region,population,currencies"}

    response = requests.get(url, headers=headers, params=params, timeout=10)
    if response.status_code == 200:
        objects = response.json()["data"]["objects"]
        return objects[0] if objects else None
    return None

def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    city = input("Enter a city name: ").strip()

    if not city:
        print("No city entered. Exiting.")
        return

    print(f"\nFetching data for {city}...")

    weather_data = get_weather(city)

    # Use the if only if you want to save the weather data.

    if weather_data:
        save_to_file(weather_data, f"{city.lower().replace(' ', '_')}_weather.json")

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}°C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown")
        currencies = country_data.get("currencies", {})
        if isinstance(currencies, dict):
            currencies = ", ".join(currencies.keys())
        print(f"\n=== Country Info ===")
        print(f"Region      : {region}")
        print(f"Population  : {population:,}")
        print(f"Currency    : {currencies}")

run_tool()