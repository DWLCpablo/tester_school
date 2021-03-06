#funkcja przymująca argument = limit, zawracająca listę z danymi jsona z API http://polakow.eu:3000/people/, modyfikowane przez podawany argument limit (okresla ile na stronie ma być obiektów)
# OMGOMGOMGOMGOMG
import hashlib
import requests

class PeopleClientError(Exception):  #ogólny błąd zapisania do API
    pass


class PeopleClient:

    # tutaj ewentualnie krotka

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

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
            people.extend(chunk) # sprawdź .extend()
        return people

    def add_person(self, first_name, last_name, email, phone, ip_address): # to nawet nieźle
        person = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone, 'ip_address': ip_address}
        headers = {'Authorization': 'Bearer ' + self.token}
        response = requests.post(self.base_url, json=person, headers=headers)
        status = response.status_code
        if not response.ok:
            raise PeopleClientError(response.json()['error'])
        return response.json()

    def person_by_id(self, person_id): # to nawet działa #DELETE bardzo podobny
        url = self.base_url + str(person_id)
        response = requests.get(url)
        if not response.ok:
            raise PeopleClientError(response.json()['error'])
        return response.json()

    def query(self, **criteria): #DZIAŁAAAAAA !!! brawo pablo
        krotka = ('first_name', 'last_name', 'phone', 'ip_address', 'email')  #można tę krotkę nawet wyrzucić na początkku, jako atrybut klasy
        for key, value in criteria.items():
            if key not in krotka:
                raise ValueError('HABLAAAAA!!!')
        response = requests.get(self.base_url, params=criteria)
        return response.json()



    def people_by_partial_ip(self, partial_ip):
        ip_regexp = '^' + partial_ip
        response = requests.get(self.base_url, params={'ip_address_like': ip_regexp})
        return response.json()


    def people_by_partial_ip1(self, partial_ip):
        response = requests.get(self.base_url, params={'ip_address_like': partial_ip})
        response['ip_address'].startswith('192.168')
        return response.json()


if __name__ == '__main__':
    token = hashlib.md5('relayr'.encode('ascii')).hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)
    #people = print(client.get_all())
    #people2 = print(client.get_all(100))
    #people3 = print(client.get_all())
    #print(people == people2)
    #person_post = print(client.add_person('pablo', 'pablo', 'cos@cos.com', '695695695', '192.192.192.192'))
    #new_person = client.add_person('pablo', 'pablo', 'coscos.com', '695695695', '192.192.192.192') #działa!!
    #print(new_person) #działa!!!
    #find_person = client.person_by_id('wKbiVtQ')
    #print(find_person)
    #print(client.query(first_name='pablo', last_name='p')) #działa, spróbuj zmienić nazwę klucza, to dostaniesz swojego errora! ;-)
    print(client.people_by_partial_ip('192.168'))
    #print(client.people_by_partial_ip1('192.168'))