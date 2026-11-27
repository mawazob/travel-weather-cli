# Travel Weather CLI

A small command-line tool that gives you a quick snapshot of any city before you travel: the live weather there, plus key facts about the country.

## The problem it solves

Planning a trip usually means opening several websites: one for the weather, another for facts like the local currency and population. This tool does both in one step. You type a city name, and it combines two live data sources into one short, readable summary and saves the full results to a file.

## What you get

- Current temperature, weather condition, humidity and wind speed (from OpenWeather)
- The country's region, population and currency (from RestCountries)
- A JSON file with the full combined data, saved in the folder where you run the tool

## Requirements

- The packages `requests` and `python-dotenv`
- Free or Premium API keys from [OpenWeather](https://openweathermap.org/api) and [RestCountries](https://restcountries.com/)

## Setup

1. Clone this repository and open the folder:

   ```bash
   git clone https://github.com/mawazob/travel-weather-cli
   cd travel-weather-cli
   ```

2. Install the packages:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a file named `.env` in the project folder with your API keys:

   ```
   OPENWEATHER_API_KEY=your_key_here
   RESTCOUNTRIES_API_KEY=your_key_here
   ```

   The `.env` file is listed in `.gitignore`, so your keys are never uploaded to GitHub.

## How to run

```bash
python travel_weather.py
```

Type a city name when asked. Example (the numbers are illustrative):

```
Travel Weather Tool
-------------------
Enter a city name: Nairobi

Fetching data for Nairobi...
Data saved to nairobi_travel_info.json

=== Nairobi, KE ===
Temperature : 22.5°C
Condition   : Scattered Clouds
Humidity    : 60%
Wind        : 3.1 m/s

=== Country Info ===
Region      : Africa
Population  : 54,000,000
Currency    : KES
```

## Where the data is saved

The full results (weather and country data together) are saved as `<city>_travel_info.json` in the folder you ran the tool from. For example, "New York" becomes `new_york_travel_info.json`.

## When something goes wrong

The tool shows a plain-language message instead of crashing when:

- no city is entered
- the city cannot be found
- the internet is down or the service is slow to respond
- your API keys are missing from `.env`
- the country details cannot be loaded (you still get the weather)