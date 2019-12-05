import requests
import json

"""
Module that will help parse the various responses depending on the queries used
for the API
"""

class ResponseParserException:
    """
    Exception handler
    """

class ResponseParser():

    def __init__(self, properties, helper):
        """
        init class for ResponseParser
        """
        self.properties = properties
        self.helper = helper

        self.api_key = self.properties['api_key']
        self.url_base = self.properties['api_url_base']

    def send_request(self, query: str):

        headers = {"Content-Type": "application/json"}
        params = {'apiKey': self.api_key}
        api_url = self.url_base + query

        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Error when running query:\n")
            print(response.text)

        return False

    def parse_recipes(self, json_response: dict):
        """
        Parse the JSON for a simple response for recipes
        """

        try:
            for recipe in json_response['results']:
                print('Title: ' + recipe['title'])
                print( 'ID: ' + str(recipe['id']) )
                print('\n-------------\n')
        except (KeyError, TypeError):
            print("No responses seen for the given search query."
                  " Please review the query.")

    def get_recipe_basic(self, query: str, count=5):
        default_query = 'search?query={0}&number={1}'.format(query, count)
        response = self.helper.send_request(default_query)

        if response:
            self.parse_recipes(response)
        else:
            print("Unable to get response from API. Please investigate connectivity")
