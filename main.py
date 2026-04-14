from weather_app_vkyei.client import OpenWeatherMap
import requests
from dotenv import load_dotenv
import os

load_dotenv(".env", override=True)  # Load environment variables from .env file

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


    
if __name__ == "__main__":
       city = input("Enter city name to get weather: ")

if not OPENWEATHER_API_KEY:
        print("❌ Missing API key")
        exit()

client = OpenWeatherMap(api_key=OPENWEATHER_API_KEY)
data = client.get_weather(city)

if "error" in data:
        print(f"❌ {data['error']}")
else:
        weather_list = data.get("weather", [])
        description = weather_list[0]["description"] if weather_list else "N/A"

        print(f"\n📍 {data['name']}")
        print(f"🌡️ Temp: {data['main']['temp']}°C")
        print(f"☁️ {description}")

try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_f = OpenWeatherMap.celsius_to_fahrenheit(temp_c)
        print(f"{temp_c}°C is {temp_f}°F")
except ValueError:
        print("❌ Please enter a valid number")