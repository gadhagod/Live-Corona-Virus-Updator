import requests
from json import loads
def data_return():
    data = loads(requests.get("https://simplecovidapi.herokuapp.com").text)
    return data['cases'], data['deaths'], data['recoveries']
