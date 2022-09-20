import unittest
from functools import reduce
import sys
sys.setrecursionlimit(100000)


class ATM:
    def __init__(self, denomination):
        self.denomination = denomination

    def get_list(self, total):
        denom = list(reduce(lambda a, acc: a + acc, map(lambda x, y: ([x] * (total // x) if (total // x) <= y
                                                                      else [x] * y)
        if x <= total else [], self.denomination.keys(),
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

    def get(self, total, num_strategy=1):
        return self.strategy(self.get_unique(total), num_strategy) if self.get_unique(
            total) != "I can't give that amount" else "I can't give that amount"

    def strategy(self, variants, num_strategy):
        if num_strategy == 1:
            return {key: min(variants, key=len).count(key) for key in min(variants, key=len)}
        elif num_strategy == 2:
            return max(({key: elem.count(key) for key in elem} for elem in variants), key=len)
        else:
            return {key: max(variants, key=len).count(key) for key in max(variants, key=len)}


class TestATM(unittest.TestCase):
    def test_get_insufficient_balance(self):
        atm = ATM({5: 1, 10: 1, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(930), "I can't give that amount")

    def test_get_5(self):
        atm = ATM({5: 2, 10: 2, 20: 2, 50: 2, 100: 2})
        self.assertEqual(atm.get_unique(5), [(5,)])
        self.assertEqual(atm.get(5), {5: 1})

    def test_get_15(self):
        atm = ATM({5: 3, 10: 2, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get_unique(15), [(10, 5), (5, 5, 5)])
        self.assertEqual(atm.get(15), {5: 1, 10: 1})
        self.assertEqual(atm.get(15, 2), {5: 1, 10: 1})
        self.assertEqual(atm.get(15, 3), {5: 3})

    def test_get_120(self):
        atm = ATM({5: 2, 10: 1, 50: 2, 60: 2, 100: 1})
        self.assertEqual(atm.get_unique(120), [(60, 50, 5, 5), (100, 10, 5, 5), (60, 50, 10), (60, 60),
                                               (50, 50, 10, 5, 5)])
        self.assertEqual(atm.get(120), {60: 2})
        self.assertEqual(atm.get(120, 2), {60: 1, 50: 1, 5: 2})
        self.assertEqual(atm.get(120, 3), {50: 2, 10: 1, 5: 2})

    def test_get_515(self):
        atm = ATM({5: 1, 10: 1, 50: 4, 100: 2, 200: 2})
        self.assertEqual(atm.get_unique(515), [(200, 100, 50, 50, 50, 50, 10, 5), (200, 100, 100, 50, 50, 10, 5),
                                               (200, 200, 100, 10, 5), (200, 200, 50, 50, 10, 5)])
        self.assertEqual(atm.get(515), {200: 2, 100: 1, 10: 1, 5: 1})
        self.assertEqual(atm.get(515, 2), {200: 1, 100: 1, 50: 4, 10: 1, 5: 1})
        self.assertEqual(atm.get(515, 3), {200: 1, 100: 1, 50: 4, 10: 1, 5: 1})

    def test_get_10(self):
        atm = ATM({5: 1, 10: 0, 20: 1, 50: 1, 100: 1})
        self.assertEqual(atm.get(10), "I can't give that amount")

    def test_get_50(self):
        atm = ATM({5: 0, 10: 0, 20: 3, 50: 0, 100: 5})
        self.assertEqual(atm.get(50), "I can't give that amount")

    def test_get_speed_after_improvements(self):
        atm = ATM({5: 6, 10: 5, 20: 2, 50: 1, 100: 1})
        self.assertEqual(atm.get_unique(30), [(20, 5, 5), (10, 5, 5, 5, 5), (10, 10, 5, 5), (20, 10), (10, 10, 10),
                                              (5, 5, 5, 5, 5, 5)])
        self.assertEqual(atm.get(30), {20: 1, 10: 1})
        self.assertEqual(atm.get(30, 2), {20: 1, 5: 2})
        self.assertEqual(atm.get(30, 3), {5: 6})

    def test_can_get_money_more_than_3000(self):
        atm = ATM({5: 100, 10: 100, 20: 100, 50: 1000, 100: 2000})
        self.assertEqual(atm.get_unique(30), [(20, 5, 5), (10, 5, 5, 5, 5), (10, 10, 5, 5), (20, 10), (10, 10, 10),
                                              (5, 5, 5, 5, 5, 5)])
        self.assertEqual(atm.get(30), {20: 1, 10: 1})

    def test_can_get_5_with_large_number_of_banknotes(self):
        atm = ATM({5: 950, 10: 10, 20: 1000, 50: 1000, 100: 2000})
        self.assertEqual(atm.get_unique(5), [(5,)])
        self.assertEqual(atm.get(5), {5: 1})

    def test_can_get_10_with_large_number_of_banknotes(self):
        atm = ATM({5: 1000, 10: 1000, 20: 1000, 50: 1000, 100: 2000})
        self.assertEqual(atm.get_unique(20), [(10, 5, 5), (5, 5, 5, 5), (20,), (10, 10)])
        self.assertEqual(atm.get(20), {20: 1})
        self.assertEqual(atm.get(20, 2), {10: 1, 5: 2})
        self.assertEqual(atm.get(20, 3), {5: 4})

    def test_can_get_5000(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 100, 200: 1000})
        self.assertEqual(atm.get(5000), {200: 25})
        self.assertEqual(atm.get(5000, 2), {100: 6, 200: 22})
        self.assertEqual(atm.get(5000, 3), {100: 14, 200: 18})

    def test_can_get_3000(self):
        atm = ATM({5: 560, 10: 500, 20: 300, 50: 500, 100: 30, 200: 1})
        self.assertEqual(atm.get(3000), {100: 28, 200: 1})
        self.assertEqual(atm.get(3000, 2), {50: 8, 100: 24, 200: 1})
        self.assertEqual(atm.get(3000, 3), {50: 8, 100: 26})


if __name__ == "__main__":
    unittest.main()
