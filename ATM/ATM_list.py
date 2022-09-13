import unittest
import sys


class ATM:
    sys.setrecursionlimit(150000)

    def __init__(self, denomination):
        self.denomination = denomination

    def get_list(self):
        denom = []
        for key, value in self.denomination.items():
            for i in range(value):
                denom.append(key)
        return denom

    def prepend(self, e, lists):
        if len(lists) == 0:
            return []
        return [[e] + lists[0]] + self.prepend(e, lists[1:])

    def duplicate(self, e, lists):
        return lists + self.prepend(e, lists)

    def f(self, d):
        if len(d) == 0:
            return [[]]
        return self.duplicate(d[0], self.f(d[1:]))

    def get(self, total):
        list_denom = self.get_list()
        list_variants = self.f(list_denom)
        res = list(filter(lambda x: x and sum(x) == total, list_variants))
        unique = set()
        for elem in res:
            unique.add(tuple(elem))
        return unique or "I can't give that amount"


class TestATM(unittest.TestCase):
    def test_get_insufficient_balance(self):
        atm = ATM({5: 1, 10: 1, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(930), "I can't give that amount")

    def test_get_5(self):
        atm = ATM({5: 2, 10: 2, 20: 2, 50: 2, 100: 2})
        self.assertEqual(atm.get(5), {(5,)})

    def test_get_15(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(15), {(5, 10), (5, 5, 5)})

    def test_get_120(self):
        atm = ATM({5: 2, 10: 1, 50: 2, 60: 2, 100: 1})
        self.assertEqual(atm.get(120), {(60, 60), (5, 5, 50, 60), (5, 5, 10, 50, 50), (10, 50, 60), (5, 5, 10, 100)})

    def test_get_675(self):
        atm = ATM({5: 1, 10: 2, 50: 5, 100: 5})
        self.assertEqual(atm.get(675), {(5, 10, 10, 50, 50, 50, 50, 50, 100, 100, 100, 100),
 (5, 10, 10, 50, 50, 50, 100, 100, 100, 100, 100)})

    def test_get_10(self):
        atm = ATM({5: 1, 10: 0, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(10), "I can't give that amount")

    def test_get_50(self):
        atm = ATM({5: 0, 10: 0, 20: 3, 50: 0, 100: 5})
        self.assertEqual(atm.get(50), "I can't give that amount")


if __name__ == "__main__":
    unittest.main()
