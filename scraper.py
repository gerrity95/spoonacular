import json
import requests

def load_props():
    try:
        with open('properties.json') as properties:
            props = json.load(properties)
    except IOError:
        print("Unable to parse properties file. Needs investigation")
        raise ScraperException

    return props

class ScraperException:
    """ Exception handler for the Scraper Class """

class Scraper:

    def __init__(self):
        self.properties = load_props()

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

    def run(self):

        recipe = self.send_request('search?query=burger&number=5')

        for i in recipe['results']:
            print(i['title'])

def main():
    app = Scraper()
    app.run()

if __name__ == '__main__':
    main()
