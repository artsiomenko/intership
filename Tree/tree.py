class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.height = 1

    def find(self, value):
        return value == self.data or \
               value < self.data and self.left and self.left.find(value) or \
               value > self.data and self.right and self.right.find(value)

    def to_list(self):
        return [self.data] + \
               (self.left.to_list() if self.left else []) + \
               (self.right.to_list() if self.right else [])

    def insert(self, new_value):
        if new_value < self.data:
            if self.left is None:
                self.left = Node(new_value)
            else:
                self.left = self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = Node(new_value)
            else:
                self.right = self.right.insert(new_value)
        return self.balance()

    def remove(self, value):
        if value < self.data:
            self.left = self.left.remove(value)
        elif value > self.data:
            self.right = self.right.remove(value)
        else:
            q = self.left
            r = self.right
            if r is None:
                return q
            min = r.findmin()
            min.right = r.removemin()
            min.left = q
            return min.balance()
        return self.balance()

    def removemin(self):
        if self.left is None:
            return self.right
        self.left = self.left.removemin()
        return self.balance()

    def findmin(self):
        return self if self.left is None else self.left.findmin()

    def balance(self):
        self.fixheight()
        if self.bfactor() == 2:
            if self.right.bfactor() < 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        if self.bfactor() == -2:
            if self.left.bfactor() > 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        return self

    def fixheight(self):
        left_height = self.left_height()
        right_height = self.right_height()
        self.height = (left_height if left_height > right_height else right_height) + 1

    def bfactor(self):
        return self.right_height() - self.left_height()

    def left_height(self):
        return self.left.height if self.left else 0

    def right_height(self):
        return self.right.height if self.right else 0

    def rotate_right(self):
        q = self.left
        self.left = q.right
        q.right = self
        self.fixheight()
        q.fixheight()
        return q

    def rotate_left(self):
        p = self.right
        self.right = p.left
        p.left = self
        self.fixheight()
        p.fixheight()
        return p

    def to_dict(self, k=0):
        d = {}
        if self.data:
            d[k] = self.data
            d['left'] = self.left.to_dict(k + 1) if self.left else {}
            d['right'] = self.right.to_dict(k + 1) if self.right else {}
        return d


class Tree:
    def __init__(self):
        self.root: Node = None

    def insert(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
        else:
            self.root = self.root.insert(new_value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def find(self, value):
        return self.root.find(value)

    def to_list(self):
        return self.root.to_list()

    def to_dict(self):
        return self.root.to_dict()


tree = Tree()
tree.insert(22)
tree.insert(11)
tree.insert(25)
tree.insert(9)
print(tree.to_dict())
