import hashlib
import json
import requests

class Account:

    def __init__(self, url):
        self.url = url

    def get_all(self):
        response = requests.get(self.url)
        return response.json()

if __name__ == '__main__':
    konto = Account('http://polakow.eu/obiekty/accounts.json')
    print(konto.get_all())