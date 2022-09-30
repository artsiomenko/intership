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


def intersections(list_meeting, n):
    people = []
    for i in range(n):
        counter = 0
        for j in range(i, n):
            if list_meeting[j].start < list_meeting[i].end:
                counter += 1
        people.append(counter)
    return max(people)


def get_max(span):
    list_start = [elem[0] for elem in span]
    list_end = [elem[1] for elem in span]
    list_meeting = []
    for i in range(len(list_start)):
        list_meeting.append(meeting(list_start[i], list_end[i], i))
    list_meeting.sort(key=lambda x: x.end)
    return intersections(list_meeting, len(list_start))


class TestLastTask(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_max([[2, 10], [3, 4], [6, 9]]), 2)

    def test_2(self):
        self.assertEqual(get_max([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]), 4)

    def test_3(self):
        self.assertEqual(get_max([[1, 8], [2, 7], [3, 5], [5, 7], [6, 7], [6, 8], [7, 8]]), 5)

    def test_datetime(self):
        x1 = datetime.time(2, 15, 00)
        y1 = datetime.time(10, 00, 00)
        x2 = datetime.time(3, 15, 00)
        y2 = datetime.time(4, 00, 00)
        x3 = datetime.time(6, 40, 00)
        y3 = datetime.time(9, 15, 10)
        self.assertEqual(get_max([[x1, y1], [x2, y2], [x3, y3]]), 2)


if __name__ == "__main__":
    unittest.main()
