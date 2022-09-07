class ATM:
    def __init__(self, name, amount, dict_denomination):
        self.name = name
        self.amount = amount
        self.dict_denomination = dict_denomination

    def get_balance(self, balance=0):
        for key, value in self.dict_denomination.items():
            balance += int(key) * value
        return balance

    def get(self, total):
        if total < self.balance:
            self.balance -= total
        else:
            return print('Insufficient balance')


dict_denom = {'5': 5, '10': 5, '20': 5, '50': 5, '100': 5}
my_card = ATM('aya', '12345678', dict_denom)
print(my_card.get_balance())
