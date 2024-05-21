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

# payload = {"api-key":"0cdce418b38aaf43b6329cf2a41521a19f2a5c64", 'page':1}
# r = requests.get('https://healthsites.io/api/v3/facilities/', params=payload)
# print(r.ok)

from coreapi import Client

client = Client()
api_key = "0cdce418b38aaf43b6329cf2a41521a19f2a5c64"
schema = client.get(f"https://healthsites.io/api/v3/facilities/?api-key={api_key}")
# schema = client.get("https://healthsites.io/api/docs/")

# Interact with the API endpoint
action = ["facilities", "list"]
params = {
    "api-key": "0cdce418b38aaf43b6329cf2a41521a19f2a5c64",
    "page": 1,
    # "country": ...,
    # "extent": ...,
    # "from": ...,
    # "to": ...,
    # "flat-properties": ...,
    # "tag-format": ...,
    # "output": ...,
}
result = client.action(schema,action, params=params)
# result = client.action(schema)

print(result)