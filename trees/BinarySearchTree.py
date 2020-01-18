class Node(object):
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value

    def add_leaf(self, value=None):
        print(value, self.value)
        if value and value > self.value:
            if self.right:
                return self.right.add_leaf(value)
            else:
                self.right = Node(value)
        else:
            if self.left:
                return self.left.add_leaf(value)
            else:
                self.left = Node(value)

    def is_leaf(self):
        return not self.right and not self.left

    def print(self):
        print(self.value)

        return '{}\t{}'.format(self.left.print() if self.left else None, self.right.print() if self.right else None)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value=None):
        if not self.root:
            self.root = Node(value)
            return
        
        return self.root.add_leaf(value)

    def print(self):
        if self.root:
            self.root.print()
        else:
            print(None)