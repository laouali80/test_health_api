import requests

r = requests.get('https://healthsites.io/api/docs/')

# print the status code
print(r)

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

def configure():
    load_dotenv()

def main():
    configure()
 

main()

client = Client()
schema = client.get("https://healthsites.io/api/docs/")

print(type(os.getenv("api_key")))
# Interact with the API endpoint
action = ["facilities", "list"]
params = {
    "api-key": os.getenv("api_key"),
    "page": 1,
    # "country": ...,
    # "extent": ...,
    # "from": ...,
    # "to": ...,
    # "flat-properties": ...,
    # "tag-format": ...,
    # "output": ...,
}
result = client.action(schema, action, params=params)
# result = client.action(schema)

# print(result)