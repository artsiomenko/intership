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
from functools import reduce


def search(list_time):
    time = reduce(lambda x, acc: acc + x, [[i for i in range(elem[0], elem[1])] for elem in list_time])
    time_dict = {key: time.count(key) for key in time}
    return max(time_dict.values())


class TestLastTask(unittest.TestCase):
    def test_1(self):
        self.assertEqual(search([[2, 10], [3, 4], [6, 9]]), 2)

    def test_2(self):
        self.assertEqual(search([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]), 4)

    def test_3(self):
        self.assertEqual(search([[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]]), 5)


if __name__ == "__main__":
    unittest.main()
