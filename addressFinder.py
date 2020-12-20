import requests
import json



URL = "https://ip-geo-location.p.rapidapi.com/ip/"


class FindToAddress():

    def __init__(self, ip_address):
        self.url = URL+ip_address
        self.querystring = {"format":"json"}

        self.headers = {
            'x-rapidapi-key': "aa69ba322fmsh8b2e5391fab5189p179a7cjsn1caca58a703c",
            'x-rapidapi-host': "ip-geo-location.p.rapidapi.com"
            }

    def find_address(self):

        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        # y=json.dumps(response.text)
        y = response.json()
        latitude = y["location"]["latitude"]
        longitude = y["location"]["longitude"]
        parameters = (latitude, longitude)
        return parameters


