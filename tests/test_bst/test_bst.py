import unittest

from bst import BinarySearchTree

class TestBstCase(unittest.TestCase):
    def test_create_tree(self):
        tree = BinarySearchTree()
        self.assertEqual(0, tree.num_nodes)

    def test_add_node(self):
        pass

    def test_remove_node(self):
        pass
    
    def test_find_node(self):
        pass