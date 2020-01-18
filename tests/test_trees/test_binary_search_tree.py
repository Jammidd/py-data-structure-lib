import unittest

from trees import BinarySearchTree

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_create_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)

    def test_add_node(self):
        value = 'Minor Node'
        self.tree.add_node(value)

        self.assertEqual(value, self.tree.root.value)
        self.assertTrue(self.tree.root.is_leaf())

    def test_add_lesser_node(self):
        tree = BinarySearchTree()
        tree.add_node('Major')
        value = 'Lesser'
        tree.add_node(value)

        self.assertIsNotNone(tree.root.left)
        self.assertEqual(value, tree.root.left.value)

    def test_add_greater_node(self):
        tree = BinarySearchTree()
        tree.add_node('Major')
        value = 'Primary'
        tree.add_node(value)

        self.assertIsNotNone(tree.root.right)
        self.assertEqual(value, tree.root.right.value)