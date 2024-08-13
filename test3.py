import requests
from config import API_TOKEN  # Import the API token from config.py

BASE_URL = "https://api.example.com/data"

def get_data(endpoint):
    headers = {
        "Authorization": f"Bearer sssdgblsibdsl/svlv;IUV;uiviubSDO;UBSD;IOBXSI;Oxbs;oisxBiosx"  # Use the token in the authorization header
    }
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"Data from {endpoint}: {data}")
    else:
        print(f"Failed to retrieve data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    endpoint = "user/profile"
    get_data(endpoint)
