import unittest
from AVLTree import Tree


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def insert_22(self):
        self.tree.insert(22)
        self.assertListEqual(self.tree.to_list(), [22])

    def insert_22_11(self):
        self.tree.insert(22)
        self.tree.insert(11)
        self.assertListEqual(self.tree.to_list(), [22, 11])

    def insert_22_11_9(self):
        self.tree.insert(22)
        self.tree.insert(11)
        self.tree.insert(9)
        self.assertListEqual(self.tree.to_list(), [11, 9, 22])

    def insert_22_11_9_4(self):
        self.tree.insert(22)
        self.tree.insert(11)
        self.tree.insert(9)
        self.tree.insert(4)
        self.assertListEqual(self.tree.to_list(), [11, 9, 4, 22])

    def insert_22_11_9_4_remove_9(self):
        self.tree.insert(22)
        self.tree.insert(11)
        self.tree.insert(9)
        self.tree.insert(4)
        self.tree.remove(9)
        self.assertListEqual(self.tree.to_list(), [11, 4, 22])


if __name__ == "__main__":
    unittest.main()
