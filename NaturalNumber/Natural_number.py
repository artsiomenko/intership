import unittest


class Zero:
    def __init__(self):
        self.parent = None

    def __eq__(self, other):
        return other

    def __add__(self, other):
        return other

    def __sub__(self, other):
        return other


class Num(Zero):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def __eq__(self, other):
        while self.parent and other.parent:
            self = self.parent
            other = other.parent
        return self.parent is None and other.parent is None

    def __add__(self, other):
        while other.parent:
            self = Num(self)
            other = other.parent
        return self

    def __sub__(self, other):
        while other.parent:
            self = self.parent
            other = other.parent
        return self


class TestNumbers(unittest.TestCase):
    def test_one_eq_one_true(self):
        one1 = Num(Zero())
        one2 = Num(Zero())
        self.assertEqual(one1 == one2, True)

    def test_one_eq_two_false(self):
        one = Num(Zero())
        two = Num(Num(Zero()))
        self.assertEqual(one == two, False)

    def test_one_add_one_eq_two(self):
        one = Num(Zero())
        two1 = one + one
        two2 = Num(Num(Zero()))
        self.assertEqual(two1 == two2, True)

    def test_two_sub_one(self):
        one = Num(Zero())
        two = Num(Num(Zero()))
        self.assertEqual(two - one == one, True)


if __name__ == "__main__":
    unittest.main()
