import requests as requests

response = requests.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Kielce&aqi=no')
print(response.json())
import requests as requests

response = requests.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Kielce&aqi=no')
dane = response.json()

with open('pogoda.json', 'w') as f:
    f.write(str(dane))
