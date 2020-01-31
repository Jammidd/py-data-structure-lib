from trees import BinarySearchTree

if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    bst.insert(10)
    bst.insert(8)

    result = bst.search(4)
    print(result)
    bst.delete(4)
    result = bst.search(4)
    print(result)
    pass
    # bst.print()