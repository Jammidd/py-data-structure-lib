from trees.Tree import Node, Tree

class TreeNode(Node):
    def __init__(self, value=None):
        self.right = None
        self.left = None
        super().__init__(value)

    def insert(self, value=None):
        if value:
            if value <= self.value:
                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = TreeNode(value)
            else:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = TreeNode(value)

    def is_leaf(self):
        return not self.right and not self.left


class BinarySearchTree(Tree):
    def insert(self, value=None):
        if not self.root:
            self.root = TreeNode(value)
            return
        
        return self.root.insert(value)

    def delete(self, value, node=-1):
        if node == -1:
            node = self.root

        if not node:
            return node

        if node.value > value:
            node.left = self.delete(value, node.left)
        elif node.value < value:
            node.right = self.delete(value, node.right)
        else:
            if not node.right:
                return node.left
            
            if not node.left:
                return node.right
            
            temp_node = node.right
            min_value = temp_node.value
            while temp_node.left:
                temp_node = temp_node.left
                min_value = temp_node.value

            node.value = min_value
            node.right = self.delete(node.value, node=node.right)
        return node

    def search(self, value, node=-1):
        node = self.root if node == -1 else node

        if not node:
            return 'Not Found'
        
        if node.value == value:
            return node.value

        if value < node.value:
            return self.search(value, node=node.left)
        
        return self.search(value, node=node.right)