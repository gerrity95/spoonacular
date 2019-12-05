import json
import requests

from response_parser import ResponseParser, ResponseParserException


class ScraperHelperException:
    """ Exception handler for the Scraper Class """

class ScraperHelper:

    def __init__(self, properties):
        self.properties = properties

        self.api_key = self.properties['api_key']
        self.url_base = self.properties['api_url_base']

    def send_request(self, query: str):

        headers = {"Content-Type": "application/json"}
        params = {'apiKey': self.api_key}
        api_url = self.url_base + query

        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Succesful Response\n")
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Error when running query:\n")
            print(response.text)

        return False
