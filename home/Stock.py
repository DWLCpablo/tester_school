import json
import copy

class Stock:

    def __init__(self, in_stock):
        self.in_stock = in_stock

    def check_stock(self):
        items = {}
        for product, number in self.in_stock.items():
            if number > 0:
                items[product] = number
        return items

    def resupply(self, product, count):
        if count <= 0:
            raise ValueError('Dodawany przedmiot musi mieć wartość dodatnią.')
        stock = self.in_stock
        stock[product] = stock.get(product, 0) + count
        return ('%s has been added. There are currently %s in stock.' % (product.title(), stock[product]))

    def withdraw(self, product, count):
        stock = self.in_stock
        if stock[product] - count < 0:
            raise ValueError('Impossibru! There aren\'t that many %s in stock. You can withdraw only as much as %s.' % (product, stock[product]))
        if product not in stock:
            raise ValueError('There\'s not any item  of that name in our stock')
        stock[product] -= count
        return '%s %s' % (count, product) + 's'', have been withdrawn. There are %s %s' % (stock[product], product)+ 's left.'


    def save_to_file(self, new_file):
        for product, count in self.in_stock.items():
            new_file.write(product + ': ' + str(count) + '\n')

    def save_to_file1(self, new_file):
        lines = [product + ': ' + str(count) + '\n' for product, count in self.in_stock.items()]
        new_file.writelines(lines)

    def to_json(self):
        return json.dumps(self.in_stock)

    @staticmethod
    def from_json(json_data):
        return json.loads(json_data)

current_stock = {'chair': 5, 'table': 3, 'bed': 4, 'lamp': 6, 'tv': 0}
my_current_stock = Stock(current_stock)
print(my_current_stock.check_stock())  # działa
print(my_current_stock.resupply('table', 4))  # działa
print(my_current_stock.check_stock())  #check
print(my_current_stock.withdraw('table', 3))  # działa
print(my_current_stock.withdraw('bed', 4))  #działa
print(my_current_stock.check_stock())  #check
with open('stock.txt', 'wt') as new_file:  # działa
    my_current_stock.save_to_file(new_file)
with open('stock_writelines.txt', 'wt') as new_file: #działa
    my_current_stock.save_to_file1(new_file)
print(my_current_stock.to_json())  #działa
print(my_current_stock.from_json(my_current_stock.to_json()))  #działa


