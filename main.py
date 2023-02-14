class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key > data:
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)

        if self.key < data:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)


root = BST(None)
root.insert(10)
print(root.l_child)
print(root.r_child)
