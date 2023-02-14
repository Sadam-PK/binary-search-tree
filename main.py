class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        

root = BST(None)
root.insert(10)
print(root.l_child)
print(root.r_child)
