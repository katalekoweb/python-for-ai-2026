import requests

# We need coordinates t get weather data

latitude = 48.85
longitude = 2.35

def get_weather (latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    # Make the request
    response = requests.get(url=url)
    data = response.json() # Dictionary
    return data['current']['temperature_2m']

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_tempo = get_weather(35.68,139.69)
benguela_temp = get_weather(-12.520501813682126, 13.400290560536657)

print(f"Paris: {paris_temp} C")
print(f"London: {london_temp} C")
print(f"Tokyo: {tokyo_tempo} C")
print(f"Benguela: {benguela_temp} C")