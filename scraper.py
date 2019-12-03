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

    def run(self):

        print(self.properties['api_key'])
        api_url_base = 'https://api.spoonacular.com/recipes/'

        headers = {"Content-Type": "application/json"}
        params = {'apiKey': self.properties['api_key']}
        api_url = api_url_base + 'search?query=cheese&number=2'
        print(api_url)

        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            print(json.loads(response.content.decode('utf-8')))
        else:
            print(response)
            print(response.text)

def main():
    app = Scraper()
    app.run()

if __name__ == '__main__':
    main()
