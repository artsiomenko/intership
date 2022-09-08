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

    def ATM_not_empty(self):
        return True if self.get_balance() > 0 else False

    def choice_of_banknotes(self, total):
        list_denom = [int(key) for key, value in self.dict_denomination.items() if self.dict_denomination[key] > 0]
        f = [1000] * (total + 1)
        f[0] = 0
        for k in range(1, total + 1):
            for i in range(len(list_denom)):
                elem = list_denom[i]
                if k - elem >= 0 and f[k - elem] < f[k]:
                    f[k] = f[k - elem]
            f[k] += 1
        result = []
        while total != 0 and self.ATM_not_empty():
            for i in range(len(list_denom)):
                elem = list_denom[i]
                if total - elem >= 0 and f[total] == f[total - elem] + 1:
                    if self.dict_denomination[elem] > 0:
                        result.append(elem)
                        total -= elem
                        self.dict_denomination[elem] -= 1
                    else:

                        continue
        return result


dict_denom = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
my_card = ATM('aya', '12345678', dict_denom)
print(my_card.get_balance())
print(my_card.get(2500))
print(my_card.get(15))
print(my_card.get(25))
print(my_card.get(60))
print(my_card.get(260))
print(my_card.dict_denomination)
print(my_card.get(10))
print(my_card.get(10))
print(my_card.get(10))
print(my_card.dict_denomination)



