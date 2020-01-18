import unittest

from bst import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_create_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(0, tree.num_nodes)

    def test_add_node(self):
        value = 'Test Node'
        self.tree.add_node(value)

        self.assertEqual(1, self.tree.num_nodes)
        self.assertEqual(value, self.tree.root.value)

    def test_remove_node(self):
        pass
    
    def test_find_node(self):
        pass