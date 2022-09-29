import unittest
from functools import reduce


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def __str__(self):
        return f"{(reduce(lambda acc, x: f'{acc} {x}', self, ''))}".lstrip()

    def __iter__(self):
        while self.head is not None:
            yield self.head.item
            self.head = self.head.next

    def search(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


class OrderedList(List):
    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            if current.item > item:
                node.next = current
                self.head = node
            else:
                while current.next and current.next.item <= item:
                    current = current.next
                node.next = current.next
                current.next = node


test_list = OrderedList()
test_list.append(1)
test_list.append(5)
test_list.append(3)
test_list.append(4)
print(test_list.__iter__())



class TestOrderedList(unittest.TestCase):
    def test_None(self):
        test_list = OrderedList()
        self.assertEqual(test_list.__str__(), '')

    def test_one_element(self):
        test_list = OrderedList()
        test_list.append(1)
        self.assertEqual(test_list.__str__(), '1')

    def test_five_elements(self):
        test_list = OrderedList()
        test_list.append(1)
        test_list.append(5)
        test_list.append(2)
        test_list.append(3)
        test_list.append(4)
        self.assertEqual(test_list.__str__(), '1 2 3 4 5')

    def test_search_true(self):
        test_list = OrderedList()
        test_list.append(1)
        test_list.append(5)
        test_list.append(2)
        test_list.append(3)
        test_list.append(4)
        self.assertTrue(test_list.search(3))

    def test_search_false(self):
        test_list = OrderedList()
        test_list.append(1)
        test_list.append(5)
        test_list.append(2)
        test_list.append(3)
        test_list.append(4)
        self.assertFalse(test_list.search(10))


if __name__ == "__main__":
    unittest.main()
