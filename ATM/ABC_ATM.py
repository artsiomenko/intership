import unittest
from functools import reduce
from abc import ABC, abstractmethod


class ATM:
    def __init__(self, denomination, abc_variant='MinimumNumberOfBanknotes'):
        self.denomination = denomination
        self.abc_variant = abc_variant

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
        return self.strategy(self.get_unique(total)) if self.get_unique(
            total) != "I can't give that amount" else "I can't give that amount"

    def strategy(self, variants):
        if self.abc_variant == 'MinimumNumberOfBanknotes':
            v1 = MinimumNumberOfBanknotes.strategy(variants)
            return v1
        if self.abc_variant == 'MaximumNumberOfKeys':
            return MaximumNumberOfKeys.strategy(variants)
        if self.abc_variant == 'MaximumNumberOfBanknotes':
            return MaximumNumberOfBanknotes.strategy(variants)


class Strategy(ABC):
    @abstractmethod
    def strategy(variants):
        pass


class MinimumNumberOfBanknotes(Strategy):
    def strategy(variants):
        return {key: min(variants, key=len).count(key) for key in min(variants, key=len)}


class MaximumNumberOfBanknotes(Strategy):
    def strategy(variants):
        return {key: max(variants, key=len).count(key) for key in max(variants, key=len)}


class MaximumNumberOfKeys(Strategy):
    def strategy(variants):
        return max(({key: elem.count(key) for key in elem} for elem in variants), key=len)


class TestATM(unittest.TestCase):
    def test_get_insufficient_balance(self):
        atm = ATM({5: 1, 10: 1, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(930), "I can't give that amount")

    def test_get_5(self):
        atm = ATM({5: 2, 10: 2, 20: 2, 50: 2, 100: 2})
        self.assertEqual(atm.get(5), {5: 1})

    def test_get_15_MinimumNumberOfBanknotes(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(15), {5: 1, 10: 1})

    def test_get_15_MaximumNumberOfBanknotes(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1}, 'MaximumNumberOfBanknotes')
        self.assertEqual(atm.get(15), {5: 3})

    def test_get_15_MaximumNumberOfKeys(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1}, 'MaximumNumberOfKeys')
        self.assertEqual(atm.get(15), {5: 1, 10: 1})

    def test_get_10(self):
        atm = ATM({5: 1, 10: 0, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(10), "I can't give that amount")

    def test_get_50(self):
        atm = ATM({5: 0, 10: 0, 20: 3, 50: 0, 100: 5})
        self.assertEqual(atm.get(50), "I can't give that amount")

    def test_get_30_MinimumNumberOfBanknotes(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1})
        self.assertEqual(atm.get(30), {20: 1, 10: 1})

    def test_get_30_MaximumNumberOfKeys(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1}, 'MaximumNumberOfKeys')
        self.assertEqual(atm.get(30), {20: 1, 5: 2})

    def test_get_30_MaximumNumberOfBanknotes(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1}, 'MaximumNumberOfBanknotes')
        self.assertEqual(atm.get(30), {5: 6})

    def test_can_get_5_with_large_number_of_banknotes(self):
        atm = ATM({5: 950, 10: 10, 20: 1000, 50: 1000, 100: 2000})
        self.assertEqual(atm.get(5), {5: 1})

    def test_can_get_5000_MinimumNumberOfBanknotes(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'MinimumNumberOfBanknotes')
        self.assertEqual(atm.get(5000), {200: 25})

    def test_can_get_5000_MaximumNumberOfKeys(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'MaximumNumberOfKeys')
        self.assertEqual(atm.get(5000), {100: 6, 200: 22})

    def test_can_get_5000_MaximumNumberOfBanknotes(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000}, 'MaximumNumberOfBanknotes')
        self.assertEqual(atm.get(5000), {100: 14, 200: 18})


if __name__ == "__main__":
    unittest.main()
