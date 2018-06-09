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
                # return self.products TWOJE


products = {'chair': 2, 'table': 3, 'lamp': 3}
stock = Stock({'chair': 2, 'table': 3, 'lamp': 3})
print(stock.products)
print(stock.resupply('bed', 5))
print(stock.available_items())
print(stock.withdraw('lamp', 8))