# gets the data from the website
import requests

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
htmlcodeline = response.text[:100001].split('\n')


def cases():
    location = htmlcodeline.index('<h1>Coronavirus Cases:</h1>')
    cases = htmlcodeline[location + 2]
    cases = cases.replace('<span style="color:#aaa">', '')
    cases = cases.replace('</span>', '')
    return cases


def deaths():
    location = htmlcodeline.index('<h1>Deaths:</h1>')
    deaths = htmlcodeline[location + 2]
    deaths = deaths.replace('<span>', '')
    deaths = deaths.replace('</span>', '')
    return deaths


def recoveries():
    location = htmlcodeline.index('<h1>Recovered:</h1>')
    recoveries = htmlcodeline[location + 2]
    recoveries = recoveries.replace('<span>', '')
    recoveries = recoveries.replace('</span>', '')
    return recoveries