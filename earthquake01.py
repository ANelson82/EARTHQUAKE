import json
import requests

# def lambda_handler(event, context):
    # Grab JSON Data from API

# url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-01-01&endtime=2020-01-02"
# response = requests.get(url).json()
f = open(usgs_api.json,)
response = json.load(f)

quake_count = response['metadata']['count']
print(quake_count)

f.close()

# quake_mag = response['features'][0]['properties']['mag']
#     print(quake_mag)
# for i in response['metadata']:
#     print(i['generated'])

