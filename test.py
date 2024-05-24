import requests

# r = requests.get('https://healthsites.io/api/docs/')

# print the status code
# print(r)

# print the method we can apply to the request
# print(dir(r))


# get more details on the method possible to the request
# print(help(r))

# to download images from a request
# r2 = requests.get('https://imgs.xkcd.com/comics/python.png')
# # print(r2.content)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)


# check the status code
# print(r.status_code)
# print(r.ok)


# get some information of the request
# print(r.headers)


# request with parameters
# payload = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get', params=payload)
# same as 
# https://httpbin.org/get?page=2&count=25
# print(r.text)
# print(r.url)
# print(r.json())


from coreapi import Client
from dotenv import load_dotenv
import os


load_dotenv()



client = Client()
schema = client.get("https://healthsites.io/api/docs/")

# Get all the health facilities
action = ["facilities", "list"]
params = {
    "api-key": os.getenv("api_key"),           # Api_key
    "page": 1,                                 # number of page
    # "country": "Nigeria",                      # Replace with the specific country name or code
    # "extent": "minLng,minLat,maxLng,maxLat", # Replace with the geographic extent (e.g., "-123.3656,48.4284,-122.3656,49.4284")
    # "from": "2024-01-01",                    # Replace with the start date in YYYY-MM-DD format
    # "to": "2024-12-31",                      # Replace with the end date in YYYY-MM-DD format
    # "flat-properties": True,                 # Boolean value to flatten properties (True/False)
    # "tag-format": "osm",                     # Tag format (e.g., "osm")
    # "output": "json"                         # Output format (e.g., "json")
}


# Get a specific health facility
# action = ["facilities", "read"]
# params = {
#     "osm_type": ...,
#     "osm_id": ...,
#     "api-key": ...,
# }


# Post an update facility (POST request)
# action = ["facilities", "read"]
# # those parameters should be in the url
# params = {
#     "osm_type": ...,
#     "osm_id": ...,
#     "api-key": ...,
# }


# Download a shapefile of a country facilities (state,local.....)
# action = ["shapefile", "download"]
# params = {
#     "country": ...,
#     "api-key": ...,
# }



result = client.action(schema, action, params=params)

print(result)