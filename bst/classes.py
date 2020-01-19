class Node(object):
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = None

    def add_leaf(self):
        pass

    def print(self):
        return print(self.value, '->', 'left:', self.left.print() if self.left else None, 'right:', self.right.print() if self.right else None) 


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.nodes = []
        self.num_nodes = 0

    def get_root_node(self):
        return self.root

    def add_node(self, value=None):
        if not self.root:
            return self.nodes.append(Node(value))
        
        print('Adding node to right or left')

    def print(self):
        for n in self.nodes:
            n.print()