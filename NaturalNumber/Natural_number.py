class NaturalNumber:
    def next(self):
       return True if Zero() else False


class Zero(NaturalNumber):
    def __init__(self, value=NaturalNumber()):
        self.value = value


zero = Zero()
one = Zero(Zero())
two = Zero(Zero(Zero()))
three = Zero(Zero(Zero(Zero())))
four = Zero(Zero(Zero(Zero(Zero()))))
print(zero.next())
print(one.next())
print(two.next())
print(three.next())
print(three.next())
print(one == two)
print(one == one)




