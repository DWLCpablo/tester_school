import json
import copy

class Stock:
    def __init__(self, products):
        self.products = dict(products) # dict(nazwa_słownika) tworzy kopię słownika na potrzeby obiektu
        # self.products = copy.deepcopy(products) # copy.deepcopy(nazwa słownika) tworzy kopię słownika na potrzeby obiektu, ale wielolevelowa

    def resupply(self, product, count):
        if count <= 0:
            raise ValueError('Można uzupełnić tylko dodatnią liczbą.')
        self.products[product] = self.products.get(product, 0) + count
        # self.products[product] += count  # tak miałeś
        return self.products

    def withdraw(self, product, count):
        if self.products[product] - count < 0:
            raise ValueError('Niewystarczająca liczba produktu w magazynie.')
        if product not in self.products:
            raise ValueError('Nie mamy takiego produktu.')
        if self.products[product] < count:
            raise ValueError('Brak wystarczającej ilości przedmiotu', product, 'w magazynie.')
        # self.products[product] - count  # Tu się wysypałeś
        self.products[product] -= count
        return self.products

    def available_items(self):
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items

    def save(self, file_obj):
        for product, count in self.products.items():
            file_obj.write(product + ',' + str(count) + '\n')


    def save2(self, file_obj):
        lines = [prod + ',' + str(count) for prod, count in self.products.items()]
        file_obj.writelines(lines)

    @staticmethod
    def load(file_obj):
        data = None
        return Stock(data)


    @staticmethod
    def foo(a): # podająć staticmethod możemyh uruchamiać funkcję na instantcjach klasy, jak i samej klasie
        print('Static method called!', a)

# JSONy
    def to_json(self):
        return json.dumps(self.products)

    @staticmethod
    def from_json(json_str):  # ??OMG
        products = json.loads(json_str)
        return Stock(products)

    def to_json_file(self, output_file):
        json.dump(self.products, output_file)

    @staticmethod
    def from_json_file(json_file):
        return Stock(json.load(json_file))

products = {'chair': 2, 'table': 3, 'lamp': 3}
stock = Stock({'chair': 2, 'table': 3, 'lamp': 3})
print(stock.products)
print(stock.resupply('bed', 5))
print(stock.available_items())
print(stock.withdraw('post', 1))
#Stock.foo('a')
#stock.foo('a')
#print(Stock.foo)
#print(stock.foo)
#with open('magazyn.csv', 'wt') as data_file:
#    stock.save(data_file)
#with open('magazyn2.csv', 'wt') as data_file:
#    stock.save2(data_file)
#print(stock.to_json())
#stock_json = stock.to_json()
#stock2 = Stock.from_json(stock_json)
#print(stock2.available_items() == stock.available_items())
#print(stock2.products == stock.products)


with open('stock.json', 'wt') as stock_json:
    stock.to_json_file(stock_json)

with open('stock.json', 'rt') as stock_json:
    stock4 = Stock.from_json_file(stock_json)

print(stock4.products)  #poważna analiza Cię tu czeka, całego pliku