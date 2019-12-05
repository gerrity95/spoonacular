import cmd
import json
import requests

from scraper_helper import ScraperHelper, ScraperHelperException
from response_parser import ResponseParser, ResponseParserException

def load_props():
    try:
        with open('properties.json') as properties:
            props = json.load(properties)
    except IOError:
        print("Unable to parse properties file. Needs investigation")
        raise ScraperException

    return props

class ScraperApp(cmd.Cmd):

    def __init__(self):

        super(ScraperApp, self).__init__()

        self.properties = load_props()
        self.helper = ScraperHelper(self.properties)
        self.parser = ResponseParser(self.properties, self.helper)

        self.api_key = self.properties['api_key']
        self.url_base = self.properties['api_url_base']

    def do_recipe_basic(self, query):
        """
        Get the top x amount of recipes for a given food type
        """
        args = query.split(' ')
        self.parser.get_recipe_basic(args[0], args[1])

    def do_exit(self, s):
        """
        Exit the application
        """
        return True

if __name__ == '__main__':
    ScraperApp().cmdloop()
