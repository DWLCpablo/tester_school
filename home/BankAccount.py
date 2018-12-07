class Account:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError('Masz debet, wynosi '+ balance)
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Wypłacana kwota musi być większa od 0.')
        elif self.balance - amount < 0:
            raise ValueError('Brak wystarczających środków na koncie')
        else:
            return self.balance - amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('ypłacana kwota musi być większa od 0.')
        else:
            return self.balance + amount

konto = Account(100)
print('Stan konta wynosi:', konto.balance)
print('Po wybraniu 20 zostało:', konto.withdraw(20))
depo = konto.deposit(30)
print('Stan konta wynosi:', depo)