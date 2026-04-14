import os
from dotenv import load_dotenv
from weather_app_vkyei.client import OpenWeatherMap

load_dotenv()

def main():
    city = input("Enter city: ")
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("❌ Missing API key")
        return

    client = OpenWeatherMap(api_key=api_key)

    try:
        data = client.get_weather(city)
        print(f"\n📍 {data['name']}")
        print(f"🌡️ Temp: {data['main']['temp']}°C")
    except Exception as e:
        print(f"❌ Error: {e}")