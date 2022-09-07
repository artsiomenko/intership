class Node:
    def __init__(self, data, init_height):
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.height = init_height

    def find(self, value):
        return value == self.data or \
               value < self.data and self.left and self.left.find(value) or \
               value > self.data and self.right and self.right.find(value)

    def to_list(self):
        return [self.data] + \
               (self.left.to_list() if self.left else []) + \
               (self.right.to_list() if self.right else [])


class Tree:
    def __init__(self):
        self.root: Node = None
        self.node_init_height = 1

    def insert(self, new_value):
        self.root = self.__insert(self.root, new_value)

    def __insert(self, p: Node, new_value):
        if p is None:
            return Node(new_value, self.node_init_height)

        if new_value < p.data:
            p.left = self.__insert(p.left, new_value)
        else:
            p.right = self.__insert(p.right, new_value)
        return self.balance(p)

    def remove(self, value):
        self.root = self.__remove(self.root, value)

    def __remove_min(self, p: Node):
        return p.right

    def findmin(self, p: Node):
        return p if p.left is None else self.findmin(p.left)

    def __remove(self, p: Node, value):
        if p is None:
            return None

        if value < p.data:
            p.left = self.__remove(p.left, value)
        elif value > p.data:
            p.right = self.__remove(p.right, value)
        else:
            q = p.left
            r = p.right
            if r is None: return q
            min = self.findmin(r)
            min.right = self.__remove_min(r)
            min.left = q
            return self.balance(min)
        return self.balance(p)

    def find(self, value):
        return self.root.find(value)

    def fixheight(self, p: Node):
        left_height = self.height(p.left)
        right_height = self.height(p.right)
        p.height = (left_height if left_height > right_height else right_height) + 1

    def rotate_right(self, p: Node):
        q = p.left
        p.left = q.right
        q.right = p
        self.fixheight(p)
        self.fixheight(q)
        return q

    def rotate_left(self, q: Node):
        p = q.right
        q.right = p.left
        p.left = q
        self.fixheight(q)
        self.fixheight(p)
        return p

    def height(self, node: Node):
        height = 0
        if node is not None:
            height = node.height
        return height

    def bfactor(self, p: Node):
        left_height = self.height(p.left)
        right_height = self.height(p.right)
        return right_height - left_height

    def balance(self, p: Node):
        self.fixheight(p)
        if self.bfactor(p) == 2:
            if self.bfactor(p.right) < 0:
                p.right = self.rotate_right(p.right)
            return self.rotate_left(p)
        if self.bfactor(p) == -2:
            if self.bfactor(p.left) > 0:
                p.left = self.rotate_left(p.left)
            return self.rotate_right(p)
        return p

    def to_list(self):
        return self.root.to_list()


tree = Tree()
tree.insert(22)
tree.insert(11)
print(True and tree.to_list())