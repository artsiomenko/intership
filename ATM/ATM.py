import unittest


class ATM:
    def __init__(self, name, dict_denomination):
        self.name = name
        self.dict_denomination = dict_denomination

    def get_balance_atm(self):
        balance = 0
        for key, value in self.dict_denomination.items():
            balance += int(key) * value
        return balance

    def get(self, total, user_balance):
        atm_balance = self.get_balance_atm()
        if user_balance <= atm_balance:
            if total <= user_balance:
                user_balance -= total
                return self.choice_of_banknotes(total), f'Users balance - {user_balance}'
            else:
                return 'Insufficient user balance'
        else:
            return 'Insufficient ATM balance'

    def atm_not_empty(self):
        return True if self.get_balance_atm() > 0 else False

    def choice_of_banknotes(self, total):
        list_denom = [key for key, value in self.dict_denomination.items() if self.dict_denomination[key] > 0]
        f = [25] * (total + 1)
        f[0] = 0
        for k in range(1, total + 1):
            for i in range(len(list_denom)):
                elem = list_denom[i]
                if k - elem >= 0 and f[k - elem] < f[k]:
                    f[k] = f[k - elem]
            f[k] += 1
        result = []
        while total != 0 and self.atm_not_empty():
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


class TestATM(unittest.TestCase):
    def test_get_balance_925(self):
        d = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
        card = ATM('aya', d)
        self.assertEqual(card.get_balance_atm(), 925)

    def test_get_insufficient_balance(self):
        d = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
        card = ATM('aya', d)
        self.assertEqual(card.get_balance_atm(), 925)
        self.assertEqual(card.get(930, 930), 'Insufficient ATM balance')

    def test_get_5(self):
        d = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
        card = ATM('aya', d)
        self.assertEqual(card.get(5, 5), ([5], 'Users balance - 0'))
        self.assertEqual(card.dict_denomination, {5: 4, 10: 5, 20: 5, 50: 5, 100: 5})

    def test_get_15(self):
        d = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
        card = ATM('aya', d)
        self.assertEqual(card.get(15, 15), ([5, 10], 'Users balance - 0'))
        self.assertEqual(card.dict_denomination, {5: 4, 10: 4, 20: 5, 50: 5, 100: 5})

    def test_get_5_15_25(self):
        d = {5: 5, 10: 5, 20: 5, 50: 5, 100: 5}
        card = ATM('aya', d)
        self.assertEqual(card.get(25, 50), ([5, 20], 'Users balance - 25'))
        self.assertEqual(card.dict_denomination, {5: 4, 10: 5, 20: 4, 50: 5, 100: 5})

if __name__ == "__main__":
    unittest.main()
