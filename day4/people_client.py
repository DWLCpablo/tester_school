#funkcja przymująca argument = limit, zawracająca listę
# OMGOMGOMGOMGOMG

import requests

class PeopleClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self, limit=None):
        if limit is None:
            response = requests.get(self.base_url).json()
            return response
        if limit <= 0:
            raise ValueError('Limit has to be positive')
        response = requests.get(self.base_url, params={'_limit': limit})
        total_records = int(response.headers['X-Total-Count'])
        pages_count = total_records // limit
        if total_records % limit != 0:
            pages_count += 1
        people = response.json()
        for page in range(2, pages_count +1):
            chunk = requests.get(self.base_url, params={'_limit': limit, '_page': page}).json()
            people.extend(chunk)
        return people

if __name__ == '__main__':
    client = PeopleClient('http://polakow.eu:3000/people/')
    people = print(client.get_all())
    people2 = print(client.get_all(100))
    people3 = print(client.get_all())

    print(people == people2)

