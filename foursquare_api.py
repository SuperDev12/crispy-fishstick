import requests
import json
latitude = 12.9716
longitude = 77.5946

url = f'https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&radius=1&categories=17069%2C13065%2C18021'
headers = {
    "accept": "application/json",
    "Authorization": "fsq37rPHo8Rsa4/EreD4ua+N1giTeAXNiqnS4mmknNtpPm8="
}

response = requests.get(url, headers=headers)

print(response.text)

if response.status_code == 200:
    with open('foursquare_response.json', 'wb') as file:
        file.write(response.content)
    print("API response saved to 'foursquare_response.json'")
else:
    print("Error:", response.status_code)


with open('foursquare_response.json', 'r') as file:
    data = json.load(file)

# Extract the keys of the JSON object
columns = data.keys()

print("Columns of the dataset:")
for column in columns:
    print(column)
    