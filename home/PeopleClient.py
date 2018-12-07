import hashlib
import json
import string
import requests

class PeopleClient:

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_all(self, limit):
        if limit is None:
            response = requests.get(self.url)
            return response.json()
        if limit <= 0:
            raise ValueError('Limit musi być liczbą dodatnią klocu!')
        response = requests.get(self.url, params={'_limit': limit})
        total_records = int(response.headers['X-Total-Count'])
        page_count = total_records // limit
        people = response.json()
        if total_records % limit == 0:
            page_count += 1
        for page in range(2, page_count + 1):
            chunk = requests.get(self.url, params={'_limit': limit, '_page': page}).json()
            people.extend(chunk) #poczytaj o extend
        return people

# zrozum to i spróbuj na Accounts

if __name__ == '__main__':
    md5 = hashlib.md5('relayr'.encode('ascii'))
    token = md5.hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)
    print(client.get_all(20))
