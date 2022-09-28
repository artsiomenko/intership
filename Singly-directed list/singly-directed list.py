import unittest


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

    def to_print(self):
        result = []
        cur = self.head
        if cur is None:
            return []
        result.append(cur.item)
        while cur.next:
            cur = cur.next
            result.append(cur.item)
        return sorted(result)

    def search(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


class TestNumbers(unittest.TestCase):
    def test_None(self):
        array = List()
        self.assertEqual(array.to_print(), [])

    def test_one_element(self):
        array = List()
        array.append(1)
        self.assertEqual(array.to_print(), [1])

    def test_five_elements(self):
        array = List()
        array.append(1)
        array.append(5)
        array.append(2)
        array.append(3)
        array.append(4)
        self.assertEqual(array.to_print(), [1, 2, 3, 4, 5])

    def test_search_true(self):
        array = List()
        array.append(1)
        array.append(5)
        array.append(2)
        array.append(3)
        array.append(4)
        self.assertTrue(array.search(3))

    def test_search_false(self):
        array = List()
        array.append(1)
        array.append(5)
        array.append(2)
        array.append(3)
        array.append(4)
        self.assertFalse(array.search(10))

    def test_to_print(self):
        array = List()
        array.append(1)
        array.append(5)
        array.append(2)
        array.append(3)
        array.append(4)
        self.assertEqual(array.to_print(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()


