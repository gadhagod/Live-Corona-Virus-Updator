# gets the data from the website
import requests


def connect():
    html_code = requests.get("https://www.worldometers.info/coronavirus/").text[:100001]
    html_code_line = html_code.split('\n')
    return html_code_line


class global_data:
    def __init__(self, code):
        self.code = code

    def cases(self):
        cases = self.code[self.code.index('<h1>Coronavirus Cases:</h1>') + 2]
        cases = cases.replace('<span style="color:#aaa">', '')
        cases = cases.replace('</span>', '')
        return cases

    def deaths(self):
        deaths = self.code[self.code.index('<h1>Deaths:</h1>') + 2]
        deaths = deaths.replace('<span>', '')
        deaths = deaths.replace('</span>', '')
        return deaths

    def recoveries(self):
        deaths = self.code[self.code.index('<h1>Recovered:</h1>') + 2]
        recoveries = recoveries.replace('<span>', '')
        recoveries = recoveries.replace('</span>', '')
        return recoveries


def data_return():
    connected = global_data(connect())
    return connected.cases(), connected.deaths(), connected.recoveries()
