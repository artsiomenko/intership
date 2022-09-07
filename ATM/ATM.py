class ATM:
    def __init__(self, name, amount, dict_denomination):
        self.name = name
        self.amount = amount
        self.dict_denomination = dict_denomination

    def get_balance(self):
        balance = 0
        for key, value in self.dict_denomination.items():
            balance += int(key) * value
        return balance

    def get(self, total):
        balance = self.get_balance()
        if total < balance:
            return self.choice_of_banknotes(total)
        else:
            return print('Insufficient balance')

    def choice_of_banknotes(self, total):
        list_denom = [int(key) for key in self.dict_denomination.keys()]
        res = []
        k = total
        while k != 0:
            for i in range(len(list_denom)):
                if k - list_denom[i] >= 0:
                    res.append(list_denom[i])
                    k -= list_denom[i]
        print(res)


dict_denom = {'5': 5, '10': 5, '20': 5, '50': 5, '100': 5}
my_card = ATM('aya', '12345678', dict_denom)
print(my_card.get_balance())
print(my_card.get(15))



