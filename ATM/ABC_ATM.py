import unittest
from functools import reduce


class ATM:
    def __init__(self, denomination, strategy='min_banknotes'):
        self.denomination = denomination
        self.strategy = strategy

    def get_list(self, total):
        denom = list(reduce(lambda a, acc: a + acc, map(lambda x, y: ([x] * (total // x) if (total // x) <= y
                                                                      else [x] * y) if x <= total else [],
                                                        self.denomination.keys(),
                                                        self.denomination.values())))
        return denom[::-1]

    def variant(self, e, lists):
        return [] if len(lists) == 0 else [[e] + lists[0]] + self.variant(e, lists[1:])

    def duplicate(self, e, lists):
        lists = [list(elem) for elem in {tuple(elem) for elem in lists}]
        return lists + self.variant(e, lists)

    def variants(self, d, total):
        return [[]] if len(d) == 0 and sum(d) < total else self.duplicate(d[0], self.variants(d[1:], total))

    def get_unique(self, total):
        res = list(filter(lambda x: x and sum(x) == total, self.variants(self.get_list(total)[:40], total)))
        unique = [elem for elem in {tuple(elem) for elem in res}]
        return unique or "I can't give that amount"

    def get(self, total):
        dict_for_get = self.withdraw(self.get_unique(total))
        if self.get_unique(total) != "I can't give that amount":
            for key, value in dict_for_get.items():
                self.denomination[key] -= value
        return dict_for_get if self.get_unique(total) != "I can't give that amount" else "I can't give that amount"

    def withdraw(self, variants):
        return Strategy.factory(self.strategy).apply_to(variants)


class Strategy:
    def factory(type):
        if type == 'min_banknotes':
            return MinBanknotes()
        if type == 'max_keys':
            return MaxKeys()
        if type == 'max_banknotes':
            return MaxBanknotes()
        return None


class MinBanknotes:
    def apply_to(self, variants):
        return {key: min(variants, key=len).count(key) for key in min(variants, key=len)}


class MaxBanknotes:
    def apply_to(self, variants):
        return {key: max(variants, key=len).count(key) for key in max(variants, key=len)}


class MaxKeys:
    def apply_to(self, variants):
        return max(({key: elem.count(key) for key in elem} for elem in variants), key=len)


class TestATM(unittest.TestCase):
    def test_get_insufficient_balance(self):
        atm = ATM({5: 1, 10: 1, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(930), "I can't give that amount")

    def test_get_5(self):
        atm = ATM({5: 2, 10: 2, 20: 2, 50: 2, 100: 2})
        self.assertEqual(atm.get(5), {5: 1})
        self.assertEqual(atm.denomination, {5: 1, 10: 2, 20: 2, 50: 2, 100: 2})

    def test_get_15_with_min_banknotes(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(15), {5: 1, 10: 1})
        self.assertEqual(atm.denomination, {5: 2, 10: 1, 20: 1, 50: 1, 100: 1})

    def test_get_10(self):
        atm = ATM({5: 1, 10: 0, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(10), "I can't give that amount")

    def test_get_50_with_min_banknotes(self):
        atm = ATM({5: 0, 10: 0, 20: 3, 50: 0, 100: 5})
        self.assertEqual(atm.get(50), "I can't give that amount")

    def test_get_30_with_min_banknotes(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1})
        self.assertEqual(atm.get(30), {20: 1, 10: 1})

    def test_get_30_with_max_keys(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1}, 'max_keys')
        self.assertEqual(atm.get(30), {20: 1, 5: 2})

    def test_get_30_with_max_banknotes(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1}, 'max_banknotes')
        self.assertEqual(atm.get(30), {5: 6})

    def test_can_get_5_with_large_number_of_banknotes(self):
        atm = ATM({5: 950, 10: 10, 20: 1000, 50: 1000, 100: 2000})
        self.assertEqual(atm.get(5), {5: 1})

    def test_can_get_5000_with_min_banknotes(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'min_banknotes')
        self.assertEqual(atm.get(5000), {200: 25})

    def test_can_get_5000_with_max_keys(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'max_keys')
        self.assertEqual(atm.get(5000), {100: 6, 200: 22})
        self.assertEqual(atm.denomination, {5: 560, 10: 500, 20: 300, 50: 500, 100: 94, 200: 978})
        self.assertEqual(atm.get(5000), {100: 6, 200: 22})
        self.assertEqual(atm.denomination, {5: 560, 10: 500, 20: 300, 50: 500, 100: 88, 200: 956})

    def test_can_get_5000_with_max_banknotes(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'max_banknotes')
        self.assertEqual(atm.get(5000), {100: 14, 200: 18})


if __name__ == "__main__":
    unittest.main()
