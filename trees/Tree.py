class Node(object):
    def __init__(self, value=None):
        self.value = value

    def insert(self, value):
        raise NotImplementedError


class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value=None):
        raise NotImplementedError

    def delete(self, value=None):
        raise NotImplementedError

    def search(self, value=None):
        raise NotImplementedError 
