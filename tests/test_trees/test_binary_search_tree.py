import unittest

from trees import BinarySearchTree

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(7)
        self.tree.insert(9)
        self.tree.insert(10)
        self.tree.insert(8)

    def test_create_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)

    def test_insert(self):
        value = 'Minor Node'
        tree = BinarySearchTree()
        tree.insert(value)

        self.assertEqual(value, tree.root.value)
        self.assertTrue(tree.root.is_leaf())

    def test_add_lesser_node(self):
        tree = BinarySearchTree()
        tree.insert('Major')
        value = 'Lesser'
        tree.insert(value)

        self.assertIsNotNone(tree.root.left)
        self.assertEqual(value, tree.root.left.value)

    def test_add_greater_node(self):
        tree = BinarySearchTree()
        tree.insert('Major')
        value = 'Primary'
        tree.insert(value)

        self.assertIsNotNone(tree.root.right)
        self.assertEqual(value, tree.root.right.value)

    def test_search_returns_node(self):
        result = self.tree.search(4)

        self.assertEqual(4, result)

    def test_search_missing_node(self):
        result = self.tree.search(12)

        self.assertEqual('Not Found', result)

    def test_delete_node(self):
        self.tree.delete(9)

        result = self.tree.search(9)

        self.assertEqual('Not Found', result)