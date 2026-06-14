import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        current = data['current_condition'][0]

        print("\n--- Weather Information ---")
        print("City:", city)
        print("Temperature:", current['temp_C'], "°C")
        print("Humidity:", current['humidity'], "%")
        print("Weather:", current['weatherDesc'][0]['value'])

    except Exception as e:
        print("Error:", e)

while True:
    city = input("\nEnter city name (or 'exit' to quit): ")

    if city.lower() == "exit":
        print("Program ended.")
        break

    get_weather(city)