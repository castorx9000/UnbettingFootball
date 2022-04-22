import requests

url = "https://api-football-v1.p.rapidapi.com/v3/predictions"

querystring = {"fixture":"198772"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "65fea5081amsh348192e8e39248cp171974jsnf611034c9af7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)