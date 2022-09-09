import unittest


class ATM:
    def __init__(self, denomination):
        self.denomination = denomination

    def get_balance(self):
        balance = 0
        for key, value in self.denomination.items():
            balance += int(key) * value
        return balance

    def get_useful_balance(self, total):
        balance = 0
        for key, value in self.denomination.items():
            if (key <= total):
                balance += int(key) * value
        return balance

    def get(self, total):
        if total <= self.get_useful_balance(total):
            result = self.choice_of_banknotes(total)
            return result if result else 'Insufficient balance'
        else:
            return 'Insufficient balance'

    def choice_of_banknotes(self, total):
        list_denom = [key for key, value in self.denomination.items() if self.denomination[key] > 0 and key <= total]
        f = [25] * (total + 1)
        f[0] = 0
        for k in range(1, total + 1):
            for i in range(len(list_denom)):
                elem = list_denom[i]
                if k - elem >= 0 and f[k - elem] < f[k]:
                    f[k] = f[k - elem]
            f[k] += 1
        result = []
        while total != 0:
            counting = False
            for i in range(len(list_denom)):
                elem = list_denom[i]
                if total - elem >= 0 and f[total] == f[total - elem] + 1:
                    if self.denomination[elem] > 0:
                        counting = True
                        result.append(elem)
                        total -= elem
                        self.denomination[elem] -= 1
            if not counting:
                break

        return result


class TestATM(unittest.TestCase):
    def test_get_balance_925(self):
        atm = ATM({5: 5, 10: 5, 20: 5, 50: 5, 100: 5})
        self.assertEqual(atm.get_balance(), 925)

    def test_get_insufficient_balance(self):
        atm = ATM({5: 5, 10: 5, 20: 5, 50: 5, 100: 5})
        self.assertEqual(atm.get_balance(), 925)
        self.assertEqual(atm.get(930), 'Insufficient balance')

    def test_get_5(self):
        atm = ATM({5: 5, 10: 5, 20: 5, 50: 5, 100: 5})
        self.assertEqual(atm.get(5), [5])
        self.assertEqual(atm.denomination, {5: 4, 10: 5, 20: 5, 50: 5, 100: 5})

    def test_get_15(self):
        atm = ATM({5: 5, 10: 5, 20: 5, 50: 5, 100: 5})
        self.assertEqual(atm.get(15), [5, 10])

    def test_get_120(self):
        atm = ATM({5: 5, 10: 5, 50: 5, 60: 5, 100: 5})
        self.assertEqual(atm.get(120), [60, 60])

    def test_get_10(self):
        atm = ATM({5: 1, 10: 0, 20: 5, 50: 5, 100: 5})
        self.assertEqual(atm.get(10), 'Insufficient balance')
        self.assertEqual(atm.denomination, {5: 1, 10: 0, 20: 5, 50: 5, 100: 5})

    def test_get_50(self):
        atm = ATM({5: 0, 10: 0, 20: 3, 50: 0, 100: 5})
        self.assertEqual(atm.get(50), 'Insufficient balance')


if __name__ == "__main__":
    unittest.main()
