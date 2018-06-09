class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError('Brak wystarcząjących na koncie.')
        self.balance = balance


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Wypłacana kwota musi być większa od 0.')
        if self.balance - amount < 0:
            raise ValueError('Brak wystarcząjących na koncie.')
        else:
            return self.balance - amount


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Wpłacana kwota musi być większa od 0.')
        return self.balance + amount

my_account = BankAccount(10)
print(my_account.balance)
print(my_account.deposit(20))
print(my_account.withdraw(50))
my_second_account = BankAccount(10)
print(my_second_account.balance)