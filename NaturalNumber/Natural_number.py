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

    def __mul__(self, other):
        return other

    def __floordiv__(self, other):
        return other


class Num:
    def __init__(self, parent):
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

    def __mul__(self, other):
        result = self
        other = other.parent
        while other.parent:
            result = Num.__add__(result, self)
            other = other.parent
        return result

    def __floordiv__(self, other):
        result = self
        other = other.parent
        while other.parent:
            result = Num.__sub__(result, self)
            other = other.parent
        return result


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
        self.assertEqual(one + Num(Zero()) == Num(Num(Zero())), True)
        self.assertEqual(one + Num(one) + Num(Zero()) == Num(Num(Num(Num(Zero())))), True)
        self.assertEqual(one == Num(Zero()), True)
        self.assertEqual(Num(Zero()) + one, Num(Num(Zero())))
        self.assertEqual(one, Num(Zero()))
        self.assertTrue(one + Zero() == one)
        self.assertTrue(Zero() + one == one)
        self.assertTrue(Zero() + Zero() == Zero())

    def test_one_eq_two_with_copy(self):
        one = Num(Zero())
        one1 = one
        two = one + one1
        self.assertEqual(two == Num(Num(Zero())), True)

    def test_two_sub_one(self):
        one = Num(Zero())
        two = Num(Num(Zero()))
        self.assertEqual(two - one == one, True)

    def test_one_mul_three(self):
        one = Num(Zero())
        three = Num(Num(Num(Zero())))
        self.assertEqual(one * three == three, True)

    def test_two_mul_three(self):
        one = Num(Zero())
        two = one + one
        three = Num(Num(Num(Zero())))
        six = three + three
        self.assertEqual(two * three == six, True)

    def test_two_mul_three_false(self):
        one = Num(Zero())
        two = one + one
        three = Num(Num(Num(Zero())))
        six = three + three
        self.assertEqual(two * three == three, False)


if __name__ == "__main__":
    unittest.main()
