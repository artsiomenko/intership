import unittest
import datetime
from functools import reduce


def get_max(list_meeting):
    hours = sorted(list({i for i in [elem[0] for elem in list_meeting] + [elem[1] for elem in list_meeting]}))
    people = []
    for hour in hours:
        counter = 0
        for j in range(len(list_meeting)):
            if list_meeting[j][0] <= hour < list_meeting[j][1]:
                counter += 1
        people.append(counter)
    return max(people)


def get_max_yet(values):
    hours = sorted(list({i for i in [elem[0] for elem in values] + [elem[1] for elem in values]}))
    return max(
        map(lambda elem: reduce(lambda acc, x: acc + 1 if x[0] <= elem <= x[1] else acc + 0, values, 0), hours))


def get_max_yet_(val):
    hours = list(map(lambda x: x[1], sorted([[x[0], 1] for x in val] + [[x[1], -1] for x in val], key=lambda x: x[0])))
    return max(reduce(lambda acc, x: acc + [sum(hours[:len(acc)])], hours, [hours[0]]))


class TestLastTask(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_max_yet_([[2, 10], [3, 4], [6, 9]]), 2)

    def test_2(self):
        self.assertEqual(get_max_yet_([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]), 5)

    def test_3(self):
        self.assertEqual(get_max_yet_([[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]]), 6)

    def test_datetime(self):
        x1 = datetime.time(2, 15, 00)
        y1 = datetime.time(10, 00, 00)
        x11 = datetime.time(2, 15, 00)
        y11 = datetime.time(10, 00, 00)
        x2 = datetime.time(3, 15, 00)
        y2 = datetime.time(4, 00, 00)
        x3 = datetime.time(6, 40, 00)
        y3 = datetime.time(9, 15, 10)
        self.assertEqual(get_max_yet_([[x1, y1], [x11, y11], [x2, y2], [x3, y3]]), 3)

    def test_22(self):
        x1 = datetime.time(2, 15, 00)
        y1 = datetime.time(3, 30, 00)
        x2 = datetime.time(3, 15, 00)
        y2 = datetime.time(4, 00, 00)
        x3 = datetime.time(2, 20, 00)
        y3 = datetime.time(3, 20, 00)
        self.assertEqual(get_max_yet_([[x1, y1], [x2, y2], [x3, y3]]), 3)


if __name__ == "__main__":
    unittest.main()
