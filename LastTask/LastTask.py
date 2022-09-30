# Дан массив временных интервалов для людей, которые заходят и выходят из комнаты. Массивы состоят из времени начала
# и окончания [[s1, e1], [s2, e2], ...] (si <ei). Какое максимальное количество людей в комнате может быть одновременно?
# Примеры:
# Ввод: [[2, 10], [3, 4], [6, 9]]
# Вывод: 2
# Ввод: [[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]
# Вывод: 4
# Ввод: [[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]]
# Вывод: 5
import unittest
import datetime


class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def intersections(l, n):
    l.sort(key=lambda x: x.end)
    max_counter = 0
    for i in range(n):
        counter = 0
        for j in range(i, n):
            if l[j].start < l[i].end:
                counter += 1
        if counter > max_counter:
            max_counter = counter
    return max_counter


def get_max(span):
    s = [elem[0] for elem in span]
    f = [elem[1] for elem in span]
    l = []
    for i in range(len(s)):
        l.append(meeting(s[i], f[i], i))
    l.sort(key=lambda x: x.end)
    return intersections(l, len(s))


class TestLastTask(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_max([[2, 10], [3, 4], [6, 9]]), 2)

    def test_2(self):
        self.assertEqual(get_max([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]), 4)

    def test_3(self):
        self.assertEqual(get_max([[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]]), 5)

    def test_datetime(self):
        x1 = datetime.time(2, 00, 00)
        y1 = datetime.time(10, 00, 00)
        x2 = datetime.time(3, 00, 00)
        y2 = datetime.time(4, 00, 00)
        x3 = datetime.time(6, 00, 00)
        y3 = datetime.time(9, 15, 10)
        self.assertEqual(get_max([[x1, y1], [x2, y2], [x3, y3]]), 2)


if __name__ == "__main__":
    unittest.main()
