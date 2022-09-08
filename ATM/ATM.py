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
        f = [1000] * (total + 1)
        f[0] = 0
        for k in range(1, total + 1):
            for i in range(len(list_denom)):
                if k - list_denom[i] >= 0 and f[k - list_denom[i]] < f[k]:
                    f[k] = f[k - list_denom[i]]
            f[k] += 1
        result = []
        while total != 0:
            for i in range(len(list_denom)):
                if total - list_denom[i] >= 0 and f[total] == f[total - list_denom[i]] + 1:
                    result.append(list_denom[i])
                    total -= list_denom[i]
        print(result)


dict_denom = {'5': 5, '10': 5, '20': 5, '50': 5, '100': 5}
my_card = ATM('aya', '12345678', dict_denom)
print(my_card.get_balance())
print(my_card.get(15))
print(my_card.get(25))
print(my_card.get(60))



