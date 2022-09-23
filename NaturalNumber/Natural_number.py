class NaturalNumber:
    def next(self):
       return True if Zero() else False


class Zero(NaturalNumber):
    def __init__(self, value=NaturalNumber()):
        self.value = value

zero = Zero()
print(zero.next())
one = Zero(Zero())
print(one.next())
two = Zero(Zero(Zero()))
print(two.next())
three = Zero(Zero(Zero(Zero())))
print(three.next())
four = Zero(Zero(Zero(Zero(Zero()))))
print(three.next())
print(one == two)
print(one == one)




