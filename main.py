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
        print(self.key, end=" ")
        if self.l_child:
            self.l_child.preorder()
        if self.r_child:
            self.r_child.preorder()

    def inorder(self):
        if self.l_child:
            self.l_child.inorder()
        print(self.key, end=" ")

        if self.r_child:
            self.r_child.inorder()

    def postorder(self):
        if self.l_child:
            self.l_child.postorder()
        if self.r_child:
            self.r_child.postorder()
        print(self.key, end=" ")

    def delete(self, data, current):
        if self.key is None:
            print("Tree is empty.")
            return
        if data < self.key:
            if self.l_child:
                self.l_child = self.l_child.delete(data, current)
            else:
                print('Required data not present in tree')
        elif data > self.key:
            if self.r_child:
                # after below recursion function, it returns NONE and is stored in the right of the parent node
                self.r_child = self.r_child.delete(data, current)
            else:
                print('Required data not present in tree')
        else:
            if self.l_child is None:
                temp = self.r_child
                if data == current:
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    temp = None
                    return
                del self
                return temp  # temp has right child of subtree, it is none, so it returns None to the parent tree left
            if self.r_child is None:
                temp = self.l_child
                if data == current:
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    temp = None
                    return
                del self
                return temp
            node = self.r_child
            while node.l_child:
                node = node.l_child
            self.key = node.key
            self.r_child = self.r_child.delete(node.key, current)
        return self


def count(nodes):
    if nodes is None:
        return 0
    return 1 + count(nodes.l_child) + count(nodes.r_child)


root = BST(10)
list_one = [5, 12, 20, 15, 40, 60, 45, 0, 40]

for i in list_one:
    root.insert(i)

root.preorder()
print()

# root.delete(20)
# print()

root.preorder()
print()
print(f'total nodes = {count(root)}')

if count(root) > 1:
    root.delete(10, root.key)
else:
    print('Cant perform deletion operation.')

print()
root.preorder()
