import requests
import json


class APIWrapper:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_data_and_save(self, filename):
            response = requests.get(self.api_url)
            response.raise_for_status()

            data = response.json()
            with open(filename, 'w') as file:
                json.dump(data, file)
            print(f'Data saved to {filename} successfully.')


if __name__ == '__main__':
    api_url = 'https://randomuser.me/api/'
    filename = 'random_user.json'

    api_wrapper = APIWrapper(api_url)
    api_wrapper.get_data_and_save(filename)
