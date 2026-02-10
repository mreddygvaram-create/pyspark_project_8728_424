import requests
import json

class AdvancedRestApiReader:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, endpoint, params=None):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    def read_all_data(self, endpoint):
        data = []
        page = 1
        while True:
            print(f"Fetching page {page}...")
            response = self.fetch_data(endpoint, params={'page': page})
            if not response or len(response) == 0:
                break
            data.extend(response)
            page += 1
        return data

    def process_data(self, raw_data):
        # Implement your data processing logic here (e.g., filtering, transforming)
        processed_data = {"data": raw_data}  # Just an example
        return processed_data

# Example usage:
# api_reader = AdvancedRestApiReader('https://api.example.com')
# all_data = api_reader.read_all_data('data_endpoint')
# processed = api_reader.process_data(all_data)

