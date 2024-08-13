import requests

# Example: Using a secret API key to access a weather API
API_KEY = "hvjvlyuvlyudcsvlysduicvsliy"  # This is your secret key; don't hard-code in real applications
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city):
    # Construct the full API request URL
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['current']['condition']['text']}, {data['current']['temp_c']}°C")
    else:
        print("Failed to retrieve weather data")

if __name__ == "__main__":
    city = "New York"
    get_weather(city)
