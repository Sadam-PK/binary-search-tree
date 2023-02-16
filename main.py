class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None  # it is a pointer having address of subtree to left
        self.r_child = None  # it is a pointer having address of subtree to right

    def insert(self, data):

        # 10
        #    # 20
        #          # 30

        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return

        if self.key > data:  # it checks if key is greater than data - subtree goes left
            if self.l_child:  # it checks if root left of BST has child tree or none?
                self.l_child.insert(data)  # if present, it calls the insert function - and imply same steps as above
            else:
                self.l_child = BST(data)  # if left pointer root is none, it adds sub tress to it along data(key/value)

        if self.key < data:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print(f'Data found! {data}')
            return
        if data < self.key:
            if self.l_child:
                self.l_child.search(data)
            else:
                print("Node is not present in the tree.")
        else:
            if self.r_child:
                self.r_child.search(data)
            else:
                print("Node is not present in the tree.")

    def preorder(self):
        print(self.key)
        if self.l_child:
            self.l_child.preorder()
        if self.r_child:
            self.r_child.preorder()


root = BST(10)
list_one = [30, 10, 60, 50, 80, 90, 0, 5]

for i in list_one:
    root.insert(i)

root.preorder()
